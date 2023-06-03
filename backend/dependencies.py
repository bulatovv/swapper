from typing import Annotated
from models import User, AuthToken
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth-tokens")


async def get_user_from_token(token: Annotated[str, Depends(oauth2_scheme)]):
    token_record = await AuthToken.get_or_none(token=token)

    if token_record is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return token_record.user


async def get_user_by_id(user_id: int):
    user = await User.get_or_none(id=user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user
