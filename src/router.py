from fastapi import APIRouter
from src.auth.routes import router as auth_router
api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=["auth"])

@api_router.get("/health")
async def health():
    return "ok"
