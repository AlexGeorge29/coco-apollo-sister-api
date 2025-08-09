from sqlalchemy import Column, String
from app.data.models.base import Base


class Gift(Base):
    __tablename__ = "gifts"

    name: Column[str] = Column(String, nullable=False)
    description: Column[str] = Column(String, nullable=True)
