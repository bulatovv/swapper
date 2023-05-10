from datetime import datetime
from enum import Enum
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from app.config import DATABASE_URL

Base = declarative_base()


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session


# CREATE TABLE "ads" (
# 	"id"	INTEGER NOT NULL UNIQUE,
# 	"name"	TEXT NOT NULL,
# 	"user_id"	INTEGER NOT NULL,
# 	"description"	INTEGER NOT NULL,
# 	"image"	TEXT NOT NULL,
# 	FOREIGN KEY("user_id") REFERENCES "users"("id"),
# 	PRIMARY KEY("id" AUTOINCREMENT)
# )
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String, nullable=False)
class Ads(Base):
    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True, autoincrement="auto", unique=True, nullable=False)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(Integer, nullable=False)
    image = Column(String, nullable=False)


# CREATE TABLE "confirms" (
# 	"your_ad_id"	INTEGER NOT NULL,
# 	"trader_ad_id"	INTEGER NOT NULL,
# 	FOREIGN KEY("trader_ad_id") REFERENCES "ads"("id"),
# 	FOREIGN KEY("your_ad_id") REFERENCES "ads"("id")
# )
class Confirms(Base):
    __tablename__ = 'confirms'
    id = Column(Integer, primary_key=True, autoincrement="auto", unique=True, nullable=False)
    your_ad_id = Column(Integer, ForeignKey('ads.id'), nullable=False)
    trader_ad_id = Column(Integer, ForeignKey('ads.id'), nullable=False)


# CREATE TABLE "offers" (
# 	"ad_id"	INTEGER NOT NULL,
# 	"trader_id"	INTEGER,
# 	FOREIGN KEY("trader_id") REFERENCES "users"("id"),
# 	FOREIGN KEY("ad_id") REFERENCES "ads"("id")
# )
class Offers(Base):
    __tablename__ = 'offers'
    id = Column(Integer, primary_key=True, autoincrement="auto", unique=True, nullable=False)
    ad_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    trader_id = Column(Integer, ForeignKey('ads.id'), nullable=True)


# CREATE TABLE sqlite_sequence(name,seq)
# тут че сделать?


# CREATE TABLE "users" (
# 	"id"	INTEGER NOT NULL UNIQUE,
# 	"name"	TEXT NOT NULL,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# )

