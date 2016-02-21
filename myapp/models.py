from mongoengine import *
from application.settings import *

connect('mytest')

class Post(Document):

    _id = StringField(max_length=10, required=True)
    full_name = StringField(max_length=50, required=True)
    phone_number = StringField(required=True)
    email = StringField(max_length=30)

