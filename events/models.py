from events import db

metadata = db.metadata

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    date_start = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)

    def __str__(self):
        return self.title


