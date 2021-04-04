from events import db
from flask_login import UserMixin

metadata = db.metadata



def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(1000), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=False)
    event_owner = db.relationship('Event', backref = 'owner')

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticate

    def is_active(self):
        """True, as all users are active."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    date_start = db.Column(db.Date)
    time_start = db.Column(db.Time)
    date_end = db.Column(db.Date)
    time_end = db.Column(db.Time)

    def __str__(self):
        return self.title


