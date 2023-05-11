from settings import settings
from tortoise import Tortoise

TORTOISE_ORM = {
    "connections" : {
        "default": settings.db_url,
    },
    "apps": {
        "models": {
            "models": [
                "models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}
