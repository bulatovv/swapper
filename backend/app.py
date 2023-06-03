from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from database import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise
from settings import settings

app = FastAPI()

origins = [
    settings.frontend_url
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    add_exception_handlers=True,
)
