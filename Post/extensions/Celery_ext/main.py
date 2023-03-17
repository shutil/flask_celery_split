from celery import Celery, Task
from extensions.Server import app
from extensions.Config import config

def Celery_ext():
    return Celery(broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERY_RESULT_BACKEND'])
    
celery = Celery_ext()