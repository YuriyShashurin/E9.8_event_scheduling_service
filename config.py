import os

class Config:

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = "manage.py"
    FLASK_DEBUG = 0
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG_TB_INTERCEPT_REDIRECTS = False
