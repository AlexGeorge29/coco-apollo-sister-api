from sqlalchemy import Column, Integer, String
from app.data.database.database import Base


class User(Base):
    __tablename__ = "users"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    username: Column[str] = Column(String, unique=True, nullable=False)
    email: Column[str] = Column(String, unique=True, nullable=False)
    passwoerd: Column[str] = Column(String, nullable=False)
