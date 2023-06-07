from typing import Annotated
from models import User, Item, AuthToken
from fastapi import HTTPException, Depends, Body, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth-tokens")


async def get_user_from_token(token: Annotated[str, Depends(oauth2_scheme)]):
    token_record = await AuthToken.get_or_none(token=token)

    if token_record is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return await token_record.user


async def get_user_by_id(user_id: int):
    user = await User.get_or_none(id=user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


async def get_user_by_id_body(user_id: Annotated[int, Body()]):
    user = await User.get_or_none(id=user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


async def get_item_by_slug_or_id(item_key: int | str):
    match (item_key):
        case int(id):
            item = await Item.get_or_none(id=id)
        case str(slug):
            item = await Item.get_or_none(slug=slug)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    return item
