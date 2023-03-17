from concurrent import futures
import time
import socket
import grpc
import sys
from grpc_server.grpc_output import post_pb2, post_pb2_grpc
import logging
import sys
import os
from extensions.Server import app
from extensions.Config import config
from extensions.Database import db
from blueprints.index.models import Post



class PostService(post_pb2_grpc.PostServicer):
    def PostExist(self,request,context):
        with app.app_context():
            exist = False
            print(request.id)
            print(type(request.id))
            pst = Post.query.filter_by(id=request.id).first()
            print(pst)
            if pst is not None:
                exist = True
            return post_pb2.PostExistReply(exist=exist)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    post_pb2_grpc.add_PostServicer_to_server(PostService(), server)
    server.add_insecure_port('[::]:8000')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    print("Grpc srver is started at port 80")
    serve()