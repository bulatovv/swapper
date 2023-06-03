from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from secrets import token_urlsafe

from tortoise.contrib.fastapi import HTTPNotFoundError

from models import (
    User, Item, Trade,
    RegistrationConfirm, RegistrationConfirm, AuthToken
)

from schemas import (
    UserRegistration, UserGet, UserUpdate,
    ItemGet,
    Item_Pydantic, User_Pydantic, UserIn_Pydantic, ItemIn_Pydantic,
    Trade_Pydantic, TradeIn_Pydantic
)
from utils import password_hash, password_verify

from dependencies import (
    get_user_by_id, get_user_from_token
)

from datetime import datetime

router = APIRouter(prefix="/api")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth-tokens")

# ALL FOR USER
# region


@router.post("/users", status_code=201, tags=["User"])
async def register_user(user_registration: UserRegistration):
    user = await User.get_or_none(email=user_registration.email)

    if user is not None:
        raise HTTPException(status_code=409, detail="Conflict")

    user = await User.create(
        email=user_registration.email,
        password_hash=user_registration.password,
        name=user_registration.name,
        verified_at=None
    )

    confirm = await RegistrationConfirm.create(
        token=token_urlsafe(32),
        user=user
    )

    # temporary confirm registration for testing
    await confirm_registration(confirm.token, user)

    return "Confirmation email sent"


@router.post(
    "/users/{user_id}/verification",
    status_code=201,
    tags=["User"]
)
async def confirm_registration(
    token: str,
    user: Annotated[User, Depends(get_user_by_id)],
):
    confirm = await RegistrationConfirm.get_or_none(
        token=token,
        user_id=user.id
    )

    if confirm is None:
        raise HTTPException(status_code=403, detail="Forbidden")

    await confirm.delete()

    user.verified_at = datetime.now()

    await user.save()


@router.get("/users", response_model=list[UserGet], tags=["User"])
async def get_users():
    return await User.all()


@router.get("/users/{user_id}", response_model=UserGet, tags=["User"])
async def get_user(user_id: int):
    user = await User.get_or_none(id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="Not found")

    return user


@router.put("/users/{user_id}", status_code=204, tags=["User"])
async def update_user(user_id: int, data: UserUpdate):
    user = await User.get_or_none(id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="Not found")

    await user.update_from_dict(data.dict()).save()


@router.delete(
    "/user/{user_id}",
    status_code=204,
    responses={404: {"model": HTTPNotFoundError}},
    tags=["User"]
)
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found"
        )


@router.post("/auth-tokens", status_code=201, tags=["User"])
async def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await User.get_or_none(email=form_data.username)

    if (
        user is None or
        not password_verify(form_data.password, user.password_hash)
    ):
        raise HTTPException(status_code=403, detail="Forbidden")

    token = await AuthToken.create(
        token=token_urlsafe(32),
        user=user
    )

    return {
        "access_token": token.token,
        "token_type": "bearer"
    }

# endregion

# ALL FOR ITEM
# region


@router.get(
    "/items",
    status_code=200,
    response_model=list[ItemGet],
    tags=["Item"]
)
async def get_items():
    return await Item.all()


@router.get(
    "/items/{item_id}",
    status_code=200,
    response_model=ItemGet,
    responses={404: {"model": HTTPNotFoundError}},
    tags=["Item"]
)
async def get_item(item_id: int):
    item = await Item.get_or_none(id=item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Not found")

    return item


@router.post("/items", status_code=201, tags=["Item"])
async def create_item(item: ItemIn_Pydantic, user_id: int):
    user = await User.get(id=user_id)
 

    item_obj = await Item.create(**item.dict(exclude_unset=True),owner=user)


@router.put("/items", status_code=201, tags=["Item"])
async def update_item(item: ItemIn_Pydantic, item_id: int):
    # ТУТ НИЧЕГО НЕ МЕНЯТЬ УЕБИЩЕ НА КЛАССЕ
    itemm = await Item.get(id=item_id)
    data = item.dict()
    print(data)
    data.pop("id")
    print(data)
    await itemm.update_from_dict(data)
    await itemm.save()
    return "1"


@router.delete("/item/{item_id}", responses={404: {"model": HTTPNotFoundError}}, tags=["Item"])
async def delete_item(item_id: int):
    deleted_count = await Item.filter(id=item_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return f"Deleted item {item_id}"

# endregion

# ALL FOR TRADE
# region

@router.get("/trades", status_code=201, response_model=list[Trade_Pydantic], tags=["Trade"])
async def get_trades():
    return await Trade_Pydantic.from_queryset(Trade.all())


@router.get("/trades/{trade_id}", status_code=201, response_model=Trade_Pydantic,
            responses={404: {"model": HTTPNotFoundError}}, tags=["Trade"])
async def get_trade(trade_id: int):
    return await Trade_Pydantic.from_queryset_single(Trade.get(id=trade_id))


@router.post("/trades", status_code=201, tags=["Trade"])
async def create_trade(trade: TradeIn_Pydantic, user_id1: int,user_id2, item_id1: int, item_id2:int):
    # Я ТУТ ВООБЩЕ НЕ ЕБУ КАК ПРАВИЛЬНО И ТД
    user1= await User.get(id=user_id1)
    user2 = await User.get(id=user_id2)
    item1 = await Item.get(id=item_id1)
    item2 = await Item.get(id=item_id2)
    trade_obj = await Trade.create(**trade.dict(exclude_unset=True))
    await trade_obj.participants.add(user1)
    await trade_obj.participants.add(user2)
    await trade_obj.items.add(item1)
    await trade_obj.items.add(item2)
    return "1"


@router.put("/trades", status_code=201, tags=["Trade"])
async def update_trade(item_id1: int, item_id2: int, trade_id:int):
    # Я ТУТ ВООБЩЕ НЕ ЕБУ КАК ПРАВИЛЬНО И ТД
    item1 = await Item.get(id=item_id1)
    item2 = await Item.get(id=item_id2)
    trade_obj= Trade(id=trade_id)
    await trade_obj.items.clear()
    await trade_obj.items.add(item1)
    await trade_obj.items.add(item2)
    await trade_obj.save()
    return "1"


@router.delete("/trades/{trade_id}", responses={404: {"model": HTTPNotFoundError}}, tags=["Trade"])
async def delete_trade(trade_id: int):
    deleted_count = await Trade.filter(id=trade_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Trade {trade_id} not found")
    return f"Deleted trade {trade_id}"

# endregion

