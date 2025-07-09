from peewee import Model, CharField, IntegerField, AutoField
from db.connection import db

class Student(Model):
    Name = CharField()
    age = IntegerField()
    email = CharField(unique=True)

    class Meta:
        database = db