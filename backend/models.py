from tortoise.models import Model
from tortoise import fields



class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(unique=True, index=True, max_length=320)
    verified_at = fields.DatetimeField(null=True)
    password_hash = fields.CharField(max_length=72)
    name = fields.TextField()
    
    items: fields.ReverseRelation["Item"]
    trades: fields.ManyToManyRelation["Trade"]

class Item(Model):
    id = fields.IntField(pk=True)
    title = fields.TextField()
    description = fields.TextField()
    image_url = fields.TextField()

    owner: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="items"
    )

class Trade(Model):
    id = fields.IntField(pk=True)
    
    participants: fields.ManyToManyRelation[User] = fields.ManyToManyField(
        "models.User", related_name="trades", through="user_trade"
    )

    items: fields.ManyToManyRelation[Item] = fields.ManyToManyField(
        "models.Item", through = "item_trade"
    )

class RegistrationConfirm(Model):
    token = fields.CharField(pk=True, index=True, max_length=64)
    user: fields.OneToOneRelation[User] = fields.OneToOneField(
        "models.User"
    )

class AuthToken(Model):
    pass
    
