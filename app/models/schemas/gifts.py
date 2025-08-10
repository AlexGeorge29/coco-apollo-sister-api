from pydantic import BaseModel, ConfigDict

from app.models.schemas.base import TimestampMixin


class GiftBase(BaseModel):

    name: str = ""
    price: int = 0
    url: str = ""
    description: str
    brand: str = ""
    img_rul: str = ""
    quantity: int = 0
    category_id: int = 0
    greatings_id: int = 0
    user_id: int = 0


class GiftModel(TimestampMixin, GiftBase):
    __tablename__ = "gifts"

    id: int
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Gift Name",
                "price": 100,
                "url": "https://example.com/gift",
                "description": "A wonderful gift",
                "brand": "Brand Name",
                "img_rul": "https://example.com/image.jpg",
                "quantity": 1,
                "category_id": 1,
                "greatings_id": 1,
                "user_id": 1,
                "created_at": "2023-10-01T12:00:00Z",
                "updated_at": "2023-10-01T12:00:00Z",
            }
        },
    )
