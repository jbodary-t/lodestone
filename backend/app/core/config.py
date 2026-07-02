from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_SQLITE_URL = f"sqlite:///{BASE_DIR / 'lodestone.db'}"


class Settings(BaseSettings):
    PROJECT_NAME: str = "Lodestone Backend"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "Backend API for activity and account management."
    DATABASE_URL: str = DEFAULT_SQLITE_URL
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = Path(__file__).resolve().parents[2] / ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
