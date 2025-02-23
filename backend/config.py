from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOSTNAME: str
    DB_PATH: str
    DATABASE_URL_NON_POOL: str

    class Config:
        env_file = ".env"


settings = Settings()