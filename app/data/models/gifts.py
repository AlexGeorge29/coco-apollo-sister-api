from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, ForeignKey

from app.data.models.base import TimestampMixin


class GiftBase(BaseModel):

    name: Column[str] = Column(String, nullable=False)
    price: Column[int] = Column(Integer, nullable=False)
    url: Column[str] = Column(String, nullable=False)
    description: Column[str] = Column(String, nullable=True)
    brand: Column[str] = Column(String, nullable=True)
    img_rul: Column[str] = Column(String, nullable=True)
    quantity: Column[int] = Column(Integer, nullable=False, default=1)
    category_id: Column[int] = Column(
        Integer, ForeignKey("categories.id"), nullable=False
    )
    greatings_id: Column[int] = Column(
        Integer, ForeignKey("greatings.id"), nullable=True
    )
    user_id: Column[int] = Column(Integer, ForeignKey("users.id"), nullable=False)


class Gift(TimestampMixin, GiftBase):
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
                "user_id": 1,
                "created_at": "2023-10-01T12:00:00Z",
                "updated_at": "2023-10-01T12:00:00Z",
            }
        },
    )
