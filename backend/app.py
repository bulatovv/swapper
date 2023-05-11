from fastapi import FastAPI
from routes import router
from database import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()

app.include_router(router)


register_tortoise(
    app,
    config=TORTOISE_ORM,
    add_exception_handlers=True,
)
