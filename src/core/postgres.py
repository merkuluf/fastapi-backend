from src.core.resource import AppResource
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker, create_async_engine
)

class Postgres(AppResource):
    engine: AsyncEngine
    session_maker: async_sessionmaker

    def __init__(
            self,
            uri: str,
            pool_size: int = 10,
            pool_timeout: int = 10,
            pool_recycle: int = 300,
    ):
        self.uri = uri
        self.pool_size = pool_size
        self.pool_timeout = pool_timeout
        self.pool_recycle = pool_recycle

    async def connect(self) -> None:
        self.engine: AsyncEngine = create_async_engine(
            self.uri,
            pool_size=self.pool_size,
        pool_timeout=self.pool_timeout,
        pool_recycle=self.pool_recycle
        )
        self.session_maker = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            future=True,
            expire_on_commit=False,
        )

    async def disconnect(self) -> None:
        await self.engine.dispose()
