from flask import Flask
from .config import DevConfig,ProductionConfig
from .extensions.database import db
from flask_migrate import Migrate

migrate=Migrate()


def create_app(config):
    app=Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app,db)
    
    return app
