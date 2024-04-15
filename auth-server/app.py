from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from database import add_user, update_user, authenticate_user, create_db
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = '34567'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app)

create_db()

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

@app.route('/update', methods=['PUT'])
@jwt_required()
def update():
    data = request.json
    username = get_jwt_identity()
    success = update_user(username, first_name=data.get('first_name'), last_name=data.get('last_name'),
                            date_of_birth=datetime.strptime(data.get('date_of_birth'), '%Y-%m-%d').date() if data.get('date_of_birth') else None,
                            email=data.get('email'), phone_number=data.get('phone_number'))
    if success:
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username and password:
        authenticated = authenticate_user(username, password)
        if authenticated:
            access_token = create_access_token(identity=username)
            return jsonify({'message': 'User authenticated successfully'}, {'access_token=': access_token}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    else:
        return jsonify({'error': 'Username and password are required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
