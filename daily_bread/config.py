import os


db_user=os.environ.get('DB_USERNAME') or 'jona'

db_password=os.environ.get('DB_PASSWORD') or 'nathanoj35'

db_name=os.environ.get('DB_NAME') or 'bible_db'

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'd70455cba20287d684fe43ab'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://{}:{}/{}'.format(db_user,db_password,db_name)
    SQLALCHEMY_ECHO=True
    DEBUG=True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'
    SQLALCHEMY_ECHO=True

class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get('PRODUCTION_DB_URI')
    DEBUG=False