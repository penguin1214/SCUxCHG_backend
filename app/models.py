# -*- coding: utf-8 -*-
from app import db

class baseEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))

    def __init__(self, username):
        self.username = username