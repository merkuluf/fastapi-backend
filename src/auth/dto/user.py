from src.core.dto_base import DTO

class CreateUser(DTO):
    init_data: str
    device: str | None = None
    timezone: str | None = None
    phone: str | None = None

class AuthResponse(DTO):
    token: str
    token_expires_in: str