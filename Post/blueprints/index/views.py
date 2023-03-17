from flask import Blueprint, jsonify, request
from extensions.Database import db
from .models import Post
from celery.result import AsyncResult
from extensions.Celery_ext import celery
from workers import create_post, update_post, delete_post

index_blp = Blueprint('index_blp',__name__)

@index_blp.get("/info")
def info():
    return jsonify({'api':'This api route is for post microservice.'})


@index_blp.post("/create")
def index():
    post_text = request.form['post_text']
    user_id = request.form['user_id']
    asy = create_post.delay(post_text=post_text,user_id=user_id)
    return jsonify({'result':'post created','result_id':asy.id})

@index_blp.post("/update/<int:id>")
def update(id):
    chk = Post.query.filter_by(id=id).first()
    if chk is not None:
        post_text = request.form['post_text']
        asy = update_post.delay(id=id,post_text=post_text)
        return jsonify({'update':'ok','result_id':asy.id})
    else:
        return jsonify({'error':'post id doesnot exist'})

@index_blp.post("/delete/<int:id>")
def delete(id):
    chk = Post.query.filter_by(id=id).first()
    if chk is not None:
        asy = delete_post.delay(id=id)
        return jsonify({'delete':'ok','result_id':asy.id})
    else:
        return jsonify({'error':'post id does not exist'})

@index_blp.get("/task_result/<id>")
def task_result(id):
    res = AsyncResult(id=id,app=celery)
    print(res.status)
    return jsonify({'task_result':res.status,'result':res.result})

@index_blp.get("/get/<int:id>")
def get_posts(id):
    pst = Post.query.filter(Post.id > id).limit(5).all()
    check_next = Post.query.filter_by(id=pst[len(pst)-1].id+1).first()
    dct = []
    for x in pst:
        post = {}
        post['id'] = x.id
        post['post_text'] = x.post_text
        post['user_id'] = x.user_id
        post['comments'] = 3
        dct.append(post)
    more = False
    if(check_next != None):
        more = True
    if more:
        return jsonify({'posts':dct,'next_id':pst[len(pst)-1].id,'more':more})
    else:
        return jsonify({'posts':dct,'more':more})
    return jsonify(dct)

