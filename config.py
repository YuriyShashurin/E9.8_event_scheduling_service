import os

class Config:

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:as89lokan07@localhost:5432/eventtt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = "app.py"
    FLASK_DEBUG = 0
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SECRET_KEY = '%RZzk)j8e*:3ZxWnr<O=TZ7K:Z<1_0/sXYL~?{Okc!GpgX"Ava2NEFQLjo}I4Iy'
    DEBUG_TB_INTERCEPT_REDIRECTS = False
