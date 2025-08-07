from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Laptop",
                "description": "Un ordinateur portable",
                "price": 999.99,
            }
        }


class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    message: str
