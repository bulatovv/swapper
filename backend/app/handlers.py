from fastapi import APIRouter, Body, Depends, HTTPException

from app.forms import *
from app.models import *
# from app.utils import get_password_hash
# from app.auth import check_auth_token
import uuid
from starlette import status

router = APIRouter()


# database =session
@router.post('/ads_create', name='ads:create')
def create_ad(ad: AdsForm = Body(..., embed=True), database=Depends(connect_db)):
    exists_ad = database.query(ad.id).one_or_none()
    if exists_ad:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='ad already exists')
    new_Ad = Ads(
        name=ad.name,
        user_id=ad.user_id,
        description=ad.description,
        image=ad.image,
    )
    database.add(new_Ad)
    database.commit()
    return {'ad_id': new_Ad.id}


@router.post('/ads_update', name='ads:update')
def update_ad(ad: AdsForm = Body(..., embed=True), database=Depends(connect_db)):
    exists_ad = database.query(ad.id).one_or_none()
    if exists_ad is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='ad dont exists')
    database.update().where(Ads.id == ad.id).values(name=ad.name,
                                                    user_id=ad.user_id,
                                                    description=ad.description,
                                                    image=ad.image)
    database.commit()
    return {'ad_id': ad}


@router.post('/ads_delete', name='ads:delete')
def delete_ad(ad: AdsForm = Body(..., embed=True), database=Depends(connect_db)):
    exists_ad = database.query(ad.id).one_or_none()
    if exists_ad is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='ad dont exists')
    database.delete(exists_ad)
    database.commit()
    return {'ad_id': ad}


@router.get('/ads_get', name='ads:get')
def get_ad(ad: AdsForm = Body(..., embed=True), database=Depends(connect_db)):
    exists_ad = database.query(ad.id).one_or_none()
    if exists_ad is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='ad dont exists')
    return {'user_id': exists_ad}


# хз чет тут делать по круду(Confirms,Offers)
# @router.post('/confirms', name='confirms:create')
# def create_user(confirm: ConfirmsForm = Body(..., embed=True), database=Depends(connect_db)):
#     exists_ad = database.query(confirm.id).one_or_none()
#     if exists_ad:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='ad already exists')
#     new_Ad = Ads(
#         name=ad.name,
#         user_id=ad.user_id,
#         description=ad.description,
#         image=ad.image,
#     )
#     database.add(new_Ad)
#     database.commit()
#     return {'ad_id': new_Ad.id}


@router.post('/user_create', name='user:create')
def create_user(user: UsersForm = Body(..., embed=True), database=Depends(connect_db)):
    exists_user = database.query(user.id).filter(Users.email == user.email).one_or_none()
    if exists_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='user already exists')
    new_user = Users(
        name=user.name
    )
    database.add(new_user)
    database.commit()
    return {'user_id': new_user.id}


@router.post('/user_update', name='user:update')
def update_user(user: UsersForm = Body(..., embed=True), database=Depends(connect_db)):
    exists_user = database.query(user.id).one_or_none()
    if exists_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='user dont exists')
    database.update().where(Users.id == user.id).values(name=user.name)
    database.commit()
    return {'user': user}


@router.post('/user_delete', name='user:delete')
def delete_user(user: UsersForm = Body(..., embed=True), database=Depends(connect_db)):
    exists_user = database.query(user.id).one_or_none()
    if exists_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='user dont exists')
    database.delete(exists_user)
    database.commit()
    return {'user_id': user}


@router.get('/user_get', name='user:get')
def get_user(user: UserCreateForm = Body(..., embed=True), database=Depends(connect_db)):
    exists_user = database.query(user.id).one_or_none()
    if exists_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='user dont exists')
    return {'user_id': user}

# @router.get('/user', name='user:get')
# def get_user(token: AuthToken = Depends(check_auth_token), database=Depends(connect_db)):
#     user = database.query(User).filter(User.id == token.user_id).one_or_none()
#
#     return {'id': user.id, 'email': user.email, 'nickname': user.nickname}
