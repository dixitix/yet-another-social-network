from concurrent import futures
import grpc

import post_pb2_grpc
import post_pb2
import database

class PostService(post_pb2_grpc.PostServiceServicer):
    def __init__(self):
        self.db = database.Database()

    def CreatePost(self, request, context):
        result = self.db.create_post(request)
        if result["success"]:
            post_data = result["post"]
            return post_pb2.OperationResponse(
                success=True,
                post=post_pb2.Post(
                    id=post_data["_id"],
                    owner_id=post_data["owner_id"],
                    title=post_data["title"],
                    content=post_data["content"]
                )
            )
        else:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(result.message)
            return post_pb2.OperationResponse(
                success=False
            )

    def UpdatePost(self, request, context):
        result = self.db.update_post(request)
        if result["success"]:
            post_data = result["post"]
            return post_pb2.OperationResponse(
                success=True,
                post=post_pb2.Post(
                    id=post_data["_id"],
                    owner_id=post_data["owner_id"],
                    title=post_data["title"],
                    content=post_data["content"]
                )
            )
        else:
            if result.message == "Permission denied":
                context.set_code(grpc.StatusCode.PERMISSION_DENIED)
                context.set_details(result.message)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(result.message)
            return post_pb2.OperationResponse(
                success=False
            )

    def DeletePost(self, request, context):
        result = self.db.delete_post(request)
        if result["success"]:
            return post_pb2.OperationResponse(
                success=True,
            )
        else:
            if result.message == "Permission denied":
                context.set_code(grpc.StatusCode.PERMISSION_DENIED)
                context.set_details(result.message)
            elif result.message == "Post not found":
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(result.message)
            else:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(result.message)
            return post_pb2.OperationResponse(
                success=False
            )

    def GetPostById(self, request, context):
        result = self.db.get_post_by_id(request)
        if result["success"]:
            post_data = result["post"]
            return post_pb2.OperationResponse(
                success=True,
                post=post_pb2.Post(
                    id=post_data["_id"],
                    owner_id=post_data["owner_id"],
                    title=post_data["title"],
                    content=post_data["content"]
                )
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(result.message)
            return post_pb2.OperationResponse(
                success=False
            )

    def ListPosts(self, request, context):
        result = self.db.list_posts(request)
        posts = []
        for post in result['posts']:
            post_message = post_pb2.Post(
                id=post["_id"],
                owner_id=post["owner_id"],
                title=post.get("title", ""),
                content=post.get("content", ""),
            )
            posts.append(post_message)
        
        return post_pb2.ListPostsResponse(
            posts=posts,
            next_page=result["next_page"]
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    post_pb2_grpc.add_PostServiceServicer_to_server(PostService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
