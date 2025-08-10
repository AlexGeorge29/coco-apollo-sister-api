from pydantic import BaseModel, ConfigDict

from app.models.schemas.base import TimestampMixin


class CategoryBase(BaseModel):

    name: str = ""
    color: str = ""
    description: str = ""


class Category(TimestampMixin, CategoryBase):
    __tablename__ = "categories"

    id: int
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Category Name",
                "couleur": "#FFFFFF",
                "description": "A brief description of the category",
            }
        },
    )
