from pymongo import MongoClient
from pymongo.collection import ReturnDocument
from bson import ObjectId
import os

class Database:
    def __init__(self):
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/blog")
        self.client = MongoClient(mongo_uri)
        self.db = self.client.blog
        self.collection = self.db.posts

    def create_post(self, request):
        """Create a new post in the posts collection"""
        post = {
            "owner_id": request.owner_id,
            "title": request.title,
            "content": request.content
        }
        result = self.collection.insert_one(post)
        if result:
            post["_id"] = str(result.inserted_id)
            return {"success": True, "post": post}
        else:
            return {"success": False, "message": "Failed to create the record in the database"}

    def update_post(self, request):
        """Update an existing post based on its ID"""
        post_id = ObjectId(request.id)
        post = self.collection.find_one({"_id": post_id})

        if not post:
            return {"success": False, "message": "Post not found"}
        if post['owner_id'] != request.user_id:
            return {"success": False, "message": "Permission denied"}
        
        update_data = {"title": request.title, "content": request.content}
        self.collection.update_one({"_id": post_id}, {"$set": update_data})
        post.update(update_data)
        post["_id"] = str(post["_id"])
        return {"success": True, "post": post}

    def delete_post(self, request):
        """Delete a post by its id"""
        post_id = ObjectId(request.id)
        post = self.collection.find_one({"_id": post_id})

        if not post:
            return {"success": False, "message": "Post not found"}
        if post['owner_id'] != request.user_id:
            return {"success": False, "message": "Permission denied"}
        
        result = self.collection.delete_one({"_id": post_id, "owner_id": request.user_id})
        
        if result.deleted_count == 0:
            return {"success": False, "message": "Failed to delete the record in the database"}

        return {"success": True}

    def get_post_by_id(self, request):
        """Query a single post by id"""
        post_id = ObjectId(request.id)
        post = self.collection.find_one({"_id": post_id})

        if not post:
            return {"success": False, "message": "Post not found"}
        if post['owner_id'] != request.user_id:
            return {"success": False, "message": "Permission denied"}
        
        post["_id"] = str(post["_id"])
        return {"success": True, "post": post}

    def list_posts(self, request):
        """List posts with pagination"""
        page_number = request.page_number
        page_size = request.page_size
        user_id = request.user_id
        
        total_documents = self.collection.count_documents({"owner_id": user_id})

        documents_to_skip = (page_number - 1) * page_size
        remaining_documents = max(total_documents - documents_to_skip, 0)

        actual_limit = min(page_size, remaining_documents)

        if actual_limit > 0:
            cursor = self.collection.find({"owner_id": user_id}).skip(documents_to_skip).limit(actual_limit)
        else:
            cursor = []

        posts = []
        
        for document in cursor:
            document["_id"] = str(document["_id"])
            posts.append(document)
        
        next_page = page_number + 1 if len(posts) == page_size else 0
        return {"posts": posts, "next_page": next_page}
