from datetime import datetime

from sqlalchemy.dialects.postgresql import JSONB
from __init__ import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    reg_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow().strftime("%d.%m.%Y %H:%M"))
    email = db.Column(db.String(120), unique=True, nullable=False)
    socials = db.Column(JSONB, unique=False, nullable=True)

    def __repr__(self):
        return f'<User id:{self.id} login:{self.login}>'
