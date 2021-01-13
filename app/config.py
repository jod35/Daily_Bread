import os

BASEDIR=os.path.dirname(os.path.realpath(__file__))




class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'd59a556cbfe0b0cec85c08b4'

class TestConfig(Config):
	SQLALCHEMY_DATABASE_URI='sqlite:///'+ os.path.join(BASEDIR,'test.db')
	SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' +os.path.join(BASEDIR,'app.db')
	DEBUG=True
