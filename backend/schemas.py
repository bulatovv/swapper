from pydantic import BaseModel, EmailStr
from typing import Optional

from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from models import User, Item, Trade

Tortoise.init_models(["models"], "models")


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    name: str


class UserGet(BaseModel):
    id: int
    email: str
    name: str


class UserUpdate(BaseModel):
    name: Optional[str]


class ItemGet(BaseModel):
    title: str
    description: str
    image_url: str

class ItemCreation(BaseModel):
    pass


# Users_Pydantic=pydantic_queryset_creator(User)
User_Pydantic=pydantic_model_creator(User)
UserIn_Pydantic = pydantic_model_creator(User, exclude_readonly=True)
Item_Pydantic = pydantic_model_creator(Item)
ItemIn_Pydantic = pydantic_model_creator(Item, exclude_readonly=True)
Trade_Pydantic = pydantic_model_creator(Trade)
TradeIn_Pydantic = pydantic_model_creator(Trade, exclude_readonly=True)
