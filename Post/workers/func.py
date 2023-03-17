from extensions.Server import app
from extensions.Config import config
from extensions.Database import db
from blueprints.index.models import Post
from celery import Celery


clry = Celery(broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERY_RESULT_BACKEND'])

@clry.task()
def create_post(post_text,user_id):
    try:
        with app.app_context():
            pst = Post(post_text=post_text,user_id=user_id)
            db.session.add(pst)
            db.session.commit()
    except Exception as e:
        print(e)
    return "ok"

@clry.task()
def update_post(id,post_text):
    with app.app_context():
        chk = Post.query.filter_by(id=id).first()
        print(chk)
        chk.post_text = post_text
        db.session.commit()
        return chk.id

@clry.task()
def delete_post(id):
    with app.app_context():
        chk = Post.query.filter_by(id=id).first()
        db.session.delete(chk)
        db.session.commit()
        return chk.id