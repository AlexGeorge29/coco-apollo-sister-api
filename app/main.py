from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.configs import configs
from .api.routes import routers

app = FastAPI(
    title=configs.PROJECT_NAME,
    description=configs.DESCRIPTION,
    debug=configs.DEBUG,
    docs_url=configs.DOCS_URL,
    version=configs.VERSION,
    openapi_url=f"{configs.API}/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=configs.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers)
