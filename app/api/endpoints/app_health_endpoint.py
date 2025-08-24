from fastapi.security import HTTPBearer

from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.models.schemas.health_model import HealthModel
from app.models.schemas.user import UserLogin

security = HTTPBearer()

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthModel)
async def health_check(
    _current_user: UserLogin = Depends(get_current_user),
) -> HealthModel:
    response = HealthModel()
    return response
