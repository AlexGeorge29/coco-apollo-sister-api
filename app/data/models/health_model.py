from pydantic import BaseModel


class HealthModel(BaseModel):
    message: str = "Healthy"
