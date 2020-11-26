from flask_migrate import Migrate

from app import create_app
from app.extensions import db
from config import Config
from worker import init_celery

config = Config()
app = create_app(config)
celery = init_celery(app, config)
migrate = Migrate(app, db)
