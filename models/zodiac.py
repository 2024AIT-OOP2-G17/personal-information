from peewee import Model, CharField
from .db import db

class Zodiac(Model):
    birthday = CharField()
    zodiac_signs = CharField()

    class Meta:
        database = db