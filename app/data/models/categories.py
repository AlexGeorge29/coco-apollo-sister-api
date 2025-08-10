from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, String


class CategoryBase(BaseModel):

    name: Column[str] = Column(String, nullable=False)
    couleur: Column[str] = Column(String, nullable=False)
    description: Column[str] = Column(String, nullable=True)


class Category(CategoryBase):
    __tablename__ = "categories"

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
