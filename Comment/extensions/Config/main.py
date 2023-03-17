from extensions.Server import app
import os

def Config():
    return app.config.from_pyfile(os.getcwd()+"/extensions/Config/config.py")

config = Config()