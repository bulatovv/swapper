from pydantic import BaseModel
from typing import Optional


class AdsForm(BaseModel):
    id: int
    name: str
    user_id: int
    description: int
    image: str


class ConfirmsForm(BaseModel):
    your_ad_id: int
    trader_ad_id: int


class OffersForm(BaseModel):
    ad_id: int
    trader_id: int


class UsersForm(BaseModel):
    id: int
    name: str


class TextGet(BaseModel):
    text: str
    phone: str
    restaurant_id: Optional[str] = None


class UserLoginForm(BaseModel):
    email: str
    password: str


class TextGet(BaseModel):
    text: str
    phone: str
    restaurant_id: Optional[str] = None


class UserCreateForm(BaseModel):
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    nickname: Optional[str] = None
