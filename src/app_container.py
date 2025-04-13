from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton, Resource

from src.auth.controller import UserController
from src.auth.user_repository import UserRepository
from src.core.postgres import Postgres
from src.settings import settings


class ApplicationContainer(DeclarativeContainer):
    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            "src.auth.routes"
        ]
    )

    postgres = Resource(Postgres.resource(), uri=settings.postgres.uri)
    user_repository = Singleton(UserRepository, postgres=postgres)
    user_controller = Singleton(UserController, user_repository=user_repository)