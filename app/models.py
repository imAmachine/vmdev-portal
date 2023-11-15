from datetime import datetime

from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import JSONB
from werkzeug.security import check_password_hash

from . import db


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String, unique=False, nullable=False)
    name = db.Column(db.String(25), unique=False, nullable=False)
    surname = db.Column(db.String(25), unique=False, nullable=False)
    reg_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow().strftime("%d.%m.%Y %H:%M"))
    email = db.Column(db.String(120), unique=True, nullable=False)
    social_links = db.Column(JSONB, unique=False, nullable=True)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User id:{self.user_id} login:{self.login}>'


class LoginUser(UserMixin):
    def __init__(self, user):
        self.id = user.user_id
        self.login = user.login
        self.name = user.name
        self.surname = user.surname
        self.email = user.email
        self.social_links = user.social_links

    @classmethod
    def get(cls, user_id):
        user = User.query.get(int(user_id))
        if user:
            return LoginUser(user)
        return None