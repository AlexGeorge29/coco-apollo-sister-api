import os
from typing import List
from pydantic import BaseModel


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


configs = Configs()
