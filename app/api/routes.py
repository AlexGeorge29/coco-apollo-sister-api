from fastapi import APIRouter

from .endpoints.gifts import router as gifts_router
from .endpoints.app_health_endpoint import router as health_router

routers = APIRouter()
router_list: list[APIRouter] = [health_router, gifts_router]

for router in router_list:
    routers.include_router(router)
