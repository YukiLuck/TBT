from mongoengine import Document, IntField
from mongoengine.fields import StringField

__all__ = ['Guild']

class Guild(Document):
    id = IntField(primary_key=True)
    prefix = StringField(min_length=1, max_length=10)
    