from pydantic import BaseModel, ConfigDict, field_validator

from app.models.schemas.base import TimestampMixin


class GiftBase(BaseModel):
    id: int
    name: str = ""
    price: int = 0
    url: str = ""
    description: str
    brand: str = ""
    img_url: str = ""
    quantity: int = 0
    category_id: int = 0
    greatings_id: int = 0
    slug: str = ""
    remaining_amount: int = 0

    @field_validator("price", "quantity", mode="before")
    @classmethod
    def validate_non_negative(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Value must be non-negative")
        return value

    @field_validator("remaining_amount", mode="before")
    @classmethod
    def validate_remaining_amount(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Remaining amount must be non-negative")
        return value


class GiftResponse(TimestampMixin, GiftBase):
    __tablename__ = "gifts"
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
                "sluf": "gift-name",
                "remaining_amount": 100,
                "created_at": "2023-10-01T12:00:00Z",
                "updated_at": "2023-10-01T12:00:00Z",
            }
        },
    )


class GiftsListResponse(BaseModel):
    gifts: list[GiftResponse] = []
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "gifts": [
                    {
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
                ],
            }
        },
    )


class GiftToUpdate(TimestampMixin, GiftBase):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Updated Gift Name",
                "price": 150,
                "url": "https://example.com/updated-gift",
                "description": "An even more wonderful gift",
                "brand": "Updated Brand Name",
                "img_rul": "https://example.com/updated-image.jpg",
                "quantity": 2,
                "category_id": 2,
                "greatings_id": 2,
            }
        },
    )
