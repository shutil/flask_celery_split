from extensions.Server import app
from extensions.Config import config
from flask import Blueprint, jsonify, request
from .models import Comment
from celery.result import AsyncResult
from extensions.Celery_ext import celery
from workers import create_comment, update_comment, delete_comment
from grpc_server import post_pb2, post_pb2_grpc
import grpc

index_blp = Blueprint('index_blp',__name__)

@index_blp.get("/info")
def info():
    return jsonify({'api':'This api route is for comment microservice.'})

@index_blp.post("/create")
def create():
    comment_text = request.form['comment_text']
    post_id = request.form['post_id']
    user_id = request.form['user_id']

    # for cheking the existance of post
    with grpc.insecure_channel("post_grpc_server:8000") as channel:
        stub = post_pb2_grpc.PostStub(channel)
        res = stub.PostExist(request=post_pb2.PostExistRequest(id=int(post_id)))
        if res.exist:
            asy = create_comment.delay(comment_text=comment_text,post_id=post_id,user_id=user_id)
            return jsonify({'res':'comment created','result_id':asy.id})
        else:
            return jsonify({'res':'error on creating comment','post':'post id does not exist'})

@index_blp.post("/update/<int:id>")
def update(id):
    chk = Comment.query.filter_by(id=id).first()
    if chk is not None:
        comment_text = request.form['comment_text']
        asy = update_comment.delay(comment_text=comment_text,id=chk.id)
        return jsonify({'api':'update successfully','result_id':asy.id})
    else:
        return jsonify({'error':'comment id doesnot exist'})

@index_blp.post("/delete/<int:id>")
def delete(id):
    chk = Comment.query.filter_by(id=id).first()
    if chk is not None:
        asy = delete_comment.delay(id=chk.id)
        return jsonify({'delete':'ok','result_id':asy.id})
    else:
        return jsonify({'error':'comment id does not exist'})

@index_blp.get("/task_result/<id>")
def task_result(id):
    res = AsyncResult(id=id,app=celery)
    print(res.status)
    print(res)
    return jsonify({'task_result':res.status})