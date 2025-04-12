from sqlalchemy import (BigInteger, Text, Boolean, DateTime, func, Integer)
from sqlalchemy.orm import Mapped, mapped_column
import zoneinfo

from src.core.models_base import Base
from datetime import datetime
from enum import Enum

class UserAccessLevel(int, Enum):
    BANNED = -1
    DEFAULT = 0
    PROMOTED = 1

class User(Base):
    __tablename__ = "users"

    tid: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    first_name: Mapped[str] = mapped_column(Text, nullable=True)
    last_name: Mapped[str] = mapped_column(Text(), nullable=True)
    username: Mapped[str] = mapped_column(Text(), nullable=True)
    language_code: Mapped[str] = mapped_column(Text(), nullable=True)
    is_premium: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    gamed_premium_until: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    photo_url: Mapped[str] = mapped_column(Text(), nullable=True)

    kind: Mapped[Integer] = mapped_column(Integer, nullable=False, server_default=str(UserAccessLevel.DEFAULT))
    registered_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        default_factory=lambda: datetime.now(tz=zoneinfo.ZoneInfo("UTC")),
        nullable=False,
    )

