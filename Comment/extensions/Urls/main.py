from extensions.Server import app
from extensions.Config import config
from blueprints.index import index_blp

def Urls():
    return [
        app.register_blueprint(index_blp,url_prefix="/comment")
    ]

urls = Urls()