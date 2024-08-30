from datetime import datetime

from mongoengine import ReferenceField, Document
from mongoengine.fields import BooleanField, StringField
from mongo_connect import connect

class Contact(Document):
    name = StringField(required=True)
    email = StringField()
    send_message = BooleanField(default=False)

