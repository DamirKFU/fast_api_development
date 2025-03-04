import fastapi

from app.api.auth.routes import router as auth_router
from app.api.routes import router as base_router

__all__ = ["api_router"]


api_router = fastapi.APIRouter()


api_router.include_router(base_router)
api_router.include_router(auth_router)
