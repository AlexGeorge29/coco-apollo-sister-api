from sqlalchemy import Column, Integer, String

from app.data.models.base import Base


class Greating(Base):
    __tablename__ = "greatings"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    name: Column[str] = Column(String, nullable=False)
    level: Column[str] = Column(String, nullable=False)
