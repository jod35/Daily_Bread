from flask import Flask
from daily_bread.config import DevConfig
from daily_bread.extensions.database import db
from flask_migrate import Migrate
from daily_bread.app.views import app_bp

import os

config=os.getenv('FLASK_ENV') or DevConfig
migrate=Migrate()

def create_app():
    app=Flask(__name__)

    app.config.from_object(config)

    app.register_blueprint(app_bp,url_prefix='/dailybread')

    with app.app_context():
        db.init_app(app)

        migrate.init_app(app,db)

    return app


    

