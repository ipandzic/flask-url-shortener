import string
from datetime import datetime
from random import choices

from .extensions import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

    def __init__(self, account_id, password):
        self.account_id = account_id
        self.password = password

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(3), unique=True)
    redirect_type = db.Column(db.Integer, default=302)
    visits = db.Column(db.Integer, default=0)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=3))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        
        return short_url
