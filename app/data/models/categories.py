from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String

from app.data.database.database import Base


class Category(Base):
    __tablename__ = "categories"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    name: Column[str] = Column(String, nullable=False)
    couleur: Column[str] = Column(String, nullable=False)
    description: Column[str] = Column(String, nullable=True)
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
