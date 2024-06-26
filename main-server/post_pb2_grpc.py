# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import post_pb2 as post__pb2


class PostServiceStub(object):
    """PostService defines the RPC methods available for interacting with posts.
    It includes operations to create new posts, retrieve, delete, update existing ones by their ID 
    and retrieving list of posts with pagination.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/post.PostService/CreatePost',
                request_serializer=post__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=post__pb2.OperationResponse.FromString,
                )
        self.UpdatePost = channel.unary_unary(
                '/post.PostService/UpdatePost',
                request_serializer=post__pb2.UpdatePostRequest.SerializeToString,
                response_deserializer=post__pb2.OperationResponse.FromString,
                )
        self.DeletePost = channel.unary_unary(
                '/post.PostService/DeletePost',
                request_serializer=post__pb2.DeletePostRequest.SerializeToString,
                response_deserializer=post__pb2.OperationResponse.FromString,
                )
        self.GetPostById = channel.unary_unary(
                '/post.PostService/GetPostById',
                request_serializer=post__pb2.GetPostByIdRequest.SerializeToString,
                response_deserializer=post__pb2.OperationResponse.FromString,
                )
        self.ListPosts = channel.unary_unary(
                '/post.PostService/ListPosts',
                request_serializer=post__pb2.ListPostsRequest.SerializeToString,
                response_deserializer=post__pb2.ListPostsResponse.FromString,
                )


class PostServiceServicer(object):
    """PostService defines the RPC methods available for interacting with posts.
    It includes operations to create new posts, retrieve, delete, update existing ones by their ID 
    and retrieving list of posts with pagination.
    """

    def CreatePost(self, request, context):
        """Creates a new post with the given owner_id, title and content, 
        returning information about successing of operation and the created post.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePost(self, request, context):
        """Updates an existing post with the given post id, user id, title and content. 
        Returns information about the success or failure of the operation and the updated post.
        The operation will only succeed if the provided user_id matches the owner_id of the post.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePost(self, request, context):
        """Deletes an existing post by the given post id and user id. Returns information about the success or failure of the operation.
        The operation will only succeed if the provided user_id matches the owner_id of the post.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPostById(self, request, context):
        """Retrieves the details of an existing post by post id and user id. 
        The operation will only succeed if the provided user_id matches the owner_id of the post.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPosts(self, request, context):
        """Lists posts with pagination by given current page number, number of posts per page and user_id. 
        Returns posts of their creator by owner_id and the next page number.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=post__pb2.CreatePostRequest.FromString,
                    response_serializer=post__pb2.OperationResponse.SerializeToString,
            ),
            'UpdatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePost,
                    request_deserializer=post__pb2.UpdatePostRequest.FromString,
                    response_serializer=post__pb2.OperationResponse.SerializeToString,
            ),
            'DeletePost': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePost,
                    request_deserializer=post__pb2.DeletePostRequest.FromString,
                    response_serializer=post__pb2.OperationResponse.SerializeToString,
            ),
            'GetPostById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPostById,
                    request_deserializer=post__pb2.GetPostByIdRequest.FromString,
                    response_serializer=post__pb2.OperationResponse.SerializeToString,
            ),
            'ListPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPosts,
                    request_deserializer=post__pb2.ListPostsRequest.FromString,
                    response_serializer=post__pb2.ListPostsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'post.PostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PostService(object):
    """PostService defines the RPC methods available for interacting with posts.
    It includes operations to create new posts, retrieve, delete, update existing ones by their ID 
    and retrieving list of posts with pagination.
    """

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/post.PostService/CreatePost',
            post__pb2.CreatePostRequest.SerializeToString,
            post__pb2.OperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/post.PostService/UpdatePost',
            post__pb2.UpdatePostRequest.SerializeToString,
            post__pb2.OperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/post.PostService/DeletePost',
            post__pb2.DeletePostRequest.SerializeToString,
            post__pb2.OperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPostById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/post.PostService/GetPostById',
            post__pb2.GetPostByIdRequest.SerializeToString,
            post__pb2.OperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/post.PostService/ListPosts',
            post__pb2.ListPostsRequest.SerializeToString,
            post__pb2.ListPostsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
