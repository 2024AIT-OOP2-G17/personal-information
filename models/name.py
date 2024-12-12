from peewee import Model, CharField, IntegerField
from .db import db

class Name(Model):
    name = CharField()
    phone = IntegerField()

    class Meta:
        database = db