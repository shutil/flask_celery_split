from extensions.Server import app
from extensions.Config import config
from extensions.Database import db
from flask_migrate import Migrate

def Migrate_ext():
    return Migrate(app=app,db=db)

migrate = Migrate_ext()