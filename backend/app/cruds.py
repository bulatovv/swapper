from datetime import datetime
from enum import Enum
from sqlalchemy import create_engine, Column,Integer,String, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from backend.app.config import DATABASE_URL
from backend.app.models import *



def create_Ad(name, email,user_id,description,image):
    new_user = Ads(name=name, email=email,user_id=user_id,description=description,image=image)
    return new_user

