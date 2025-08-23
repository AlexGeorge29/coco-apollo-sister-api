from fastapi import APIRouter

from .endpoints.gifts import router as gifts_router
from .endpoints.gift_user import router as gift_user_router
from .endpoints.app_health_endpoint import router as health_router
from .endpoints.users import router as users_router

routers = APIRouter()
router_list: list[APIRouter] = [
    health_router,
    gifts_router,
    gift_user_router,
    users_router,
]

for router in router_list:
    routers.include_router(router)
