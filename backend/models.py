from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(unique=True, index=True, max_length=320)
    name = fields.TextField()



class Item(Model):
     id = fields.IntField(pk=True)
     title = fields.TextField()
     description = fields.TextField()
     image_url = fields.TextField()



class Trade(Model):
    id = fields.IntFields(pk=True)
