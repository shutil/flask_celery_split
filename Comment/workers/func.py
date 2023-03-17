from extensions.Server import app
from extensions.Config import config
from extensions.Database import db
from blueprints.index.models import Comment
from celery import Celery

clry = Celery(broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERY_RESULT_BACKEND'])

@clry.task()
def create_comment(comment_text,post_id,user_id):
    with app.app_context():
        cmt = Comment(comment_text=comment_text,post_id=post_id,user_id=user_id)
        db.session.add(cmt)
        db.session.commit()
        
        return cmt.id

@clry.task()
def update_comment(id,comment_text):
    with app.app_context():
        chk = Comment.query.filter_by(id=id).first()
        chk.comment_text = comment_text
        db.session.commit()
        return chk.id

@clry.task()
def delete_comment(id):
    with app.app_context():
        dl = Comment.query.filter_by(id=id).first()
        db.session.delete(dl)
        db.session.commit()
        return dl.id