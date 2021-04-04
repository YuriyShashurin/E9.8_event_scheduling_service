import os

class Config:

    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgres://fqyswquqxqdlhn:d98455ef32eb7575a145638d0cc0f027d78e48c8f7f309799f4efc0f443a43b4@ec2-3-233-43-103.compute-1.amazonaws.com:5432/dac2db4dpvmdpv'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = "app.py"
    FLASK_DEBUG = 0
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SECRET_KEY = '%RZzk)j8e*:3ZxWnr<O=TZ7K:Z<1_0/sXYL~?{Okc!GpgX"Ava2NEFQLjo}I4Iy'
    DEBUG_TB_INTERCEPT_REDIRECTS = False
