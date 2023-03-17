from flask_migrate import Migrate
from extensions.Server import app
from extensions.Config import config
from extensions.Database import db


def Migrate_ext():
    return Migrate(app,db)

migrate = Migrate_ext()