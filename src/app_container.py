from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton

from src.auth.controller import UserController
from src.auth.user_repository import UserRepository


class ApplicationContainer(DeclarativeContainer):
    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            "src.auth.routes"
        ]
    )

    user_repository = Singleton(UserRepository)
    user_controller = Singleton(UserController, user_repository=user_repository)