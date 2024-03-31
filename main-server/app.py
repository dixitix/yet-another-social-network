from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from database import add_user, update_user, authenticate_user, create_db, User
from datetime import datetime, timedelta
import os
import grpc

import post_pb2
import post_pb2_grpc

create_db()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = '34567'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app)

post_server_host = os.environ.get('POST_SERVER_HOST', 'localhost')
post_server_port = os.environ.get('POST_SERVER_PORT', '50051')

channel = grpc.insecure_channel(f'{post_server_host}:{post_server_port}')
post_service_stub = post_pb2_grpc.PostServiceStub(channel)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username and password:
        success = add_user(username, password, first_name=data.get('first_name'), last_name=data.get('last_name'),
                           date_of_birth=datetime.strptime(data.get('date_of_birth'), '%Y-%m-%d').date() if data.get('date_of_birth') else None,
                           email=data.get('email'), phone_number=data.get('phone_number'))
        if success:
            return jsonify({'message': 'User registered successfully'}), 201
        else:
            return jsonify({'error': 'Username already exists'}), 400
    else:
        return jsonify({'error': 'Username and password are required'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username and password:
        authenticated = authenticate_user(username, password)
        if authenticated:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    else:
        return jsonify({'error': 'Username and password are required'}), 400
    
@app.route('/update', methods=['PUT'])
def update():
    data = request.json
    username = data.get('username')
    if username:
        success = update_user(username, first_name=data.get('first_name'), last_name=data.get('last_name'),
                              date_of_birth=datetime.strptime(data.get('date_of_birth'), '%Y-%m-%d').date() if data.get('date_of_birth') else None,
                              email=data.get('email'), phone_number=data.get('phone_number'))
        if success:
            return jsonify({'message': 'User updated successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Username is required'}), 400

@app.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.json
    cur_user_id = get_jwt_identity()
    try:
        response = post_service_stub.CreatePost(post_pb2.CreatePostRequest(
            owner_id=cur_user_id,
            title=data.get('title'),
            content=data.get('content')
        ))
        if response.success:
            return jsonify({'id': response.post.id}), 201
        else:
            return jsonify({'error': 'Failed to create post'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/posts/<post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    data = request.json
    cur_user_id = get_jwt_identity()
    try:
        response = post_service_stub.UpdatePost(post_pb2.UpdatePostRequest(
            id=post_id,
            user_id=cur_user_id,
            title=data.get('title'),
            content=data.get('content')
        ))
        if response.success:
            return jsonify({'message': 'Post updated successfully'}), 200
        else:
            return jsonify({'error': 'Failed to update post'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/posts/<post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    cur_user_id = get_jwt_identity()
    try:
        response = post_service_stub.DeletePost(post_pb2.DeletePostRequest(id=post_id, user_id=cur_user_id))
        if response.success:
            return jsonify({'message': 'Post deleted successfully'}), 200
        else:
            return jsonify({'error': 'Failed to delete post'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/posts/<post_id>', methods=['GET'])
@jwt_required()
def get_post(post_id):
    cur_user_id = get_jwt_identity()
    try:
        response = post_service_stub.GetPost(post_pb2.GetPostByIdRequest(id=post_id, user_id=cur_user_id))
        if response.post:
            post_data = {
                'id': response.post.id,
                'owner_id': response.post.owner_id,
                'title': response.post.title,
                'content': response.post.content
            }
            return jsonify(post_data), 200
        else:
            return jsonify({'error': 'Post not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/posts', methods=['GET'])
@jwt_required()
def list_posts():
    cur_user_id = get_jwt_identity()
    page = request.args.get('page', default=1, type=int)
    try:
        response = post_service_stub.ListPosts(post_pb2.ListPostsRequest(user_id=cur_user_id, page=page, page_size=5))
        posts_data = [{
            'id': post.id,
            'owner_id': post.owner_id,
            'title': post.title,
            'content': post.content
        } for post in response.posts]
        return jsonify(posts_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
