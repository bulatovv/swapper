from pydantic import (
    BaseSettings,
    AnyUrl,
    Field
)

class Settings(BaseSettings):
    db_url: AnyUrl = Field(..., env="DB_URL")

    class Config:
        env_file='.env'

settings: Settings = Settings()
