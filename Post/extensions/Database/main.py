from flask_sqlalchemy import SQLAlchemy
from extensions.Server import app
from extensions.Config import config

def Database():
    return SQLAlchemy(app)

db = Database()