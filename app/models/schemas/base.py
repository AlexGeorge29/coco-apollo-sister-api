from datetime import datetime, timezone

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TimestampMixin:
    created_at: str = datetime.now(timezone.utc).isoformat()
    updated_at: str = datetime.now(timezone.utc).isoformat()
