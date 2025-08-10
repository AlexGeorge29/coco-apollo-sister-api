from pydantic import BaseModel, ConfigDict

from app.models.schemas.base import TimestampMixin


class HealthModelBase(BaseModel):
    message: str = "Healthy"


class HealthModel(TimestampMixin, HealthModelBase):
    __tablename__ = "health"

    id: int = 0
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "message": "Healthy",
                "created_at": "2023-10-01T12:00:00Z",
                "updated_at": "2023-10-01T12:00:00Z",
            }
        },
    )
