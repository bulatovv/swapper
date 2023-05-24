from typing import Annotated, List

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from secrets import token_urlsafe
from models import User, Item, Trade, RegistrationConfirm, RegistrationConfirm, AuthToken, Users_Pydantic
from schemas import UserRegistration, ItemCreation
from utils import password_hash, password_verify
from datetime import datetime

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth-tokens")

@router.post("/users", status_code=201)
async def register_user(user_registration: UserRegistration):
    
    user = await User.create(
        email=user_registration.username,
        password_hash=user_registration.password,
        name=user_registration.name,
        verified_at = None
    )

    confirm = await RegistrationConfirm.create(
        token = token_urlsafe(32),
        user=user
    )

    print(confirm.token) # TODO: Send this token to the user's email

    return f"Registration confirmation sent"



@router.post("/users/{user_id}/verification", status_code=201)
async def confirm_registration(token: str, user_id:int):
    user = await User.get_or_none(id=user_id)

    if user is None:
        return HTTPException(status_code=404, detail="Not found")

    confirm = await RegistrationConfirm.get_or_none(
        token=token,
        user_id=user_id
    )

    if confirm is None:
        raise HTTPException(status_code=403, detail="Forbidden")

    user.verified_at = datetime.now()

    await user.save()




# @router.get("/items", status_code=201,response_model=Users_Pydantic)
# async def get_items():
#     return await Users_Pydantic.from_queryset(User.all())
@router.post("/items", status_code=201,response_model=Users_Pydantic)
async def get_items():
    return await Users_Pydantic.from_queryset(User.all())
@router.post("/auth-tokens", status_code=201)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(email=form_data.username)

    if user is None:
        raise HTTPException(status_code=404, detail="Not found")

    if not password_verify(form_data.password, user.password_hash):
        raise HTTPException(status_code=403, detail="Forbidden")

    token = await AuthToken.create(
        token=token_urlsafe(32),
        user=user
    )
    
    return {
        "access_token": token.token,
        "token_type": "bearer"
    }
