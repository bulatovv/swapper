from pydantic import BaseModel, Field, fields
from typing import Optional
from datetime import datetime, timezone



class UserRegistration(BaseModel):
    username: str
    password: str
    name: str

class ItemCreation(BaseModel):
    ... # TODO: Create schema for item creation


