from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.app_container import ApplicationContainer
from src.auth.controller import UserController
from src.auth.dto.user import CreateUser, AuthResponse

router = APIRouter()

@router.post("/auth")
@inject
async def auth(
        create_user_playload: CreateUser,
        user_controller: UserController = Depends(Provide(ApplicationContainer.user_controller)),
) -> AuthResponse:
    await user_controller.login(create_user_playload)
    return AuthResponse(
        token='123',
        token_expires_in='321'
    )