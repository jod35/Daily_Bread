from flask import Flask
from .extensions import db
from .config import DevConfig
from .models import Record
from .api import api_bp
from .ui import ui_bp
from flask_fontawesome import FontAwesome

def create_app():
    app = Flask(__name__,static_folder='./static')

   

    app.config.from_object(DevConfig)

    db.init_app(app)

    fa=FontAwesome(app)

    app.register_blueprint(api_bp,url_prefix='/api')
    
    app.register_blueprint(ui_bp,url_prefix='/')

    @app.shell_context_processor
    def make_shell_context():
        return {
            'app': app,
            'db': db,
            'Record': Record,

        }

    return app
