from extensions.Server import app
from extensions.Config import config
from flask_sqlalchemy import SQLAlchemy

def Database():
    return SQLAlchemy(app)

db = Database()