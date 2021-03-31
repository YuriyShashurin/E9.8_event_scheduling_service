from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)