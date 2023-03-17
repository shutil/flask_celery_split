from extensions.Server import app
from extensions.Config import config
from extensions.Database import db
from extensions.Migrate import migrate
from extensions.Celery_ext import celery
from extensions.Urls import urls

if __name__ == "__main__":
    app.run(debug=True,port=8001,host='0.0.0.0')