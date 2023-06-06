from pydantic import (
    BaseSettings,
    AnyUrl,
    AnyHttpUrl,
    Field
)

from typing import Any


class Settings(BaseSettings):
    db_url: AnyUrl = Field(..., env="DB_URL")
    frontend_url: AnyHttpUrl = Field(..., env="FRONTEND_URL")
    slug_length: int = 48
    allowed_img_hosts: list[str] = Field(..., env="ALLOWED_IMG_HOSTS")

    class Config:
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            if field_name == "allowed_img_hosts":
                return [x.strip() for x in raw_val.split(",")]

            return cls.json_loads(raw_val)

        env_file = '.env'


settings: Settings = Settings()
