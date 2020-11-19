from flask_migrate import Migrate

from app import create_app
from app.extensions import db
from config import Config

config = Config()
app = create_app(config)
migrate = Migrate(app, db)
