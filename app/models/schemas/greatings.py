from pydantic import BaseModel, ConfigDict


class GreatingBase(BaseModel):

    name: str = ""
    level: str = ""


class Greating(GreatingBase):
    __tablename__ = "greatings"

    id: int
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
