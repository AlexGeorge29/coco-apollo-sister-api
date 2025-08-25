from fastapi.security import HTTPBearer

from fastapi import APIRouter
from app.models.schemas.health_model import HealthModel

security = HTTPBearer()

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthModel)
async def health_check() -> HealthModel:
    response = HealthModel()
    return response
