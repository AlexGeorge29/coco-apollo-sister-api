from fastapi import APIRouter
from .endpoints.app_health_endpoint import router as health_router

routers = APIRouter()
router_list: list[APIRouter] = [health_router]

for router in router_list:
    routers.include_router(router)
