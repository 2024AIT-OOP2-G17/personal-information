from peewee import Model, CharField, IntegerField
from .db import db
from .name import Name

class Prefecture(Model):
    area = CharField()
    num = IntegerField()

    class Meta:
        database = db