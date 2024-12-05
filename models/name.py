from peewee import Model, CharField
from .db import db

class Name(Model):
    name = CharField()
    phone = CharField()

    class Meta:
        database = db