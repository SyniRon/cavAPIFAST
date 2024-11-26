from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import username

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

#API routers
app.include_router(username.router, prefix="/api/v1/milpac/profile", tags=["milpac"])