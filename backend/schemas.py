from pydantic import BaseModel, Field, fields
from typing import Optional
from datetime import datetime, timezone

from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_queryset_creator, pydantic_model_creator

from models import User, Item, Trade

Tortoise.init_models(["models"], "models")

class UserRegistration(BaseModel):
    username: str
    password: str
    name: str

class ItemCreation(BaseModel):
    ... # TODO: Create schema for item creation


# Users_Pydantic=pydantic_queryset_creator(User)
User_Pydantic=pydantic_model_creator(User)
UserIn_Pydantic = pydantic_model_creator(User, exclude_readonly=True)
Item_Pydantic = pydantic_model_creator(Item)
ItemIn_Pydantic = pydantic_model_creator(Item, exclude_readonly=True)
Trade_Pydantic = pydantic_model_creator(Trade)
TradeIn_Pydantic = pydantic_model_creator(Trade, exclude_readonly=True)
