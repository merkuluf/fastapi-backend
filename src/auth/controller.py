from fastapi import  HTTPException, status
from src.auth.dto.user import CreateUser
from src.auth.user_repository import UserRepository
from aiogram.utils.web_app import safe_parse_webapp_init_data

class UserController:
    def __init__(
            self,
            user_repository: UserRepository,
    ):
        self.user_repository = user_repository

    async def login(self, payload: CreateUser) -> bool:
        try:
            data = safe_parse_webapp_init_data(token='', init_data=payload.init_data)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid_init_data")
        if data.user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="init_data_missing_user")

        # referrer_tid, ref_source = self._parse_start_param(data.start_param)
        # await self.user_repository.referrer_check(payload)

        return True

    @staticmethod
    def _parse_start_param(start_param: str | None) -> tuple[int | None, str | None]:
        if not start_param:
            return None, None

        if start_param.startswith("refstory"):
            prefix = "refstory"
            ref_source = "story"
        elif start_param.startswith("ref"):
            prefix = "ref"
            ref_source = None
        else:
            return None, None

        try:
            return int(start_param.replace(prefix, "")), ref_source
        except ValueError:
            return None, None