from peewee import Model, CharField,IntegerField
from .db import db

class Zodiac(Model):
    birthday = IntegerField()
    zodiac_signs = CharField()

    class Meta:
        database = db