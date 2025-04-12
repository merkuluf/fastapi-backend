import os

import sentry_sdk
from datetime import timedelta
from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

class PostgresSettings(BaseSettings):
    host: str
    port: int = 5432
    db: str
    user: str
    password: str

    @property
    def uri(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@" f"{self.host}:{self.port}/{self.db}"


class ServerSettings(BaseSettings):
    reload: bool = False
    public_url: str

class AuthSettings(BaseSettings):
    secret: str
    jwt_algorithm: str = "HS256"
    token_ttl: timedelta = timedelta(hours=12)

class SentrySettings(BaseSettings):
    dsn: str | None = None

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__", extra="ignore")

    log_level: str = "warning"
    env: str = "local"
    debug: bool = False

    server: ServerSettings
    postgres: PostgresSettings
    auth: AuthSettings
    sentry: SentrySettings = SentrySettings()

try:
    settings = AppSettings(_env_file=os.getenv("ENV_FILE"))
except ValidationError:
    if os.getenv("ENV") == "test":
        settings = None  # type: ignore[assignment]
    else:
        raise

else:
    if settings.sentry.dsn is not None:
        sentry_sdk.init(
            dsn=settings.sentry.dsn,
            enable_tracing=False,
            environment=settings.env,
        )
