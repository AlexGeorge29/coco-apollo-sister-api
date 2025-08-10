from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, String


class GreatingBase(BaseModel):

    name: Column[str] = Column(String, nullable=False)
    level: Column[str] = Column(String, nullable=False)


class Greating(GreatingBase):
    __tablename__ = "greatings"

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "from_attributes": True,
            "json_schema_extra": {
                "example": {
                    "id": 1,
                    "name": "Hello",
                    "level": "friendly",
                }
            },
        },
    )
