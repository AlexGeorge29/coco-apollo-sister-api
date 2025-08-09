from gotrue import BaseModel
from sqlalchemy import Column, Integer, String


class Gift(BaseModel):
    __tablename__ = "gifts"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    name: Column[str] = Column(String, nullable=False)
    description: Column[str] = Column(String, nullable=True)
