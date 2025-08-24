import os
from typing import List
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class Configs(BaseModel):
    API: str = "/api"
    VERSION: str = "1.0.0"
    PROJECT_NAME: str = "coco-apollo-sister-api"
    DESCRIPTION: str = "API for bith list backend"

    PROJECT_ROOT: str = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    DEBUG: bool = False
    DOCS_URL: str = "/docs"

    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # Supabase
    SUPABASE_URL: str | None = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str | None = os.getenv("SUPABASE_KEY")
    SUPABASE_SERVICE_KEY: str | None = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    # Database
    DATABASE_URL: str | None = os.getenv("DATABASE_URL")
    DB_HOST: str | None = os.getenv("DB_HOST")
    DB_PORT: int | None = int(os.getenv("DB_PORT", "5432"))
    DB_USER: str | None = os.getenv("DB_USER")
    DB_PASSWORD: str | None = os.getenv("DB_PASSWORD")
    DB_NAME: str | None = os.getenv("DB_NAME")

    class Config:
        env_file = ".env"


configs = Configs()
