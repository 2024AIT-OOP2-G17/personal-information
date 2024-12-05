from peewee import Model, CharField, IntegerField
from .db import db

class User(Model):
    birthday = CharField()
    zodiac_signs = CharField()

    class Meta:
        database = db