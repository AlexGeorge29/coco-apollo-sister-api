from fastapi import APIRouter
from app.data.models.health_model import HealthModel


router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthModel)
async def health_check() -> HealthModel:
    response = HealthModel()
    return response
