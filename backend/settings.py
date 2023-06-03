from pydantic import (
    BaseSettings,
    AnyUrl,
    AnyHttpUrl,
    Field
)


class Settings(BaseSettings):
    db_url: AnyUrl = Field(..., env="DB_URL")
    frontend_url: AnyHttpUrl = Field(..., env="FRONTEND_URL")

    class Config:
        env_file = '.env'


settings: Settings = Settings()
