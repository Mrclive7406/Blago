from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """Модель для чтения пользователя."""


class UserCreate(schemas.BaseUserCreate):
    """Модель для создания нового пользователя."""


class UserUpdate(schemas.BaseUserUpdate):
    """Модель для обновления информации о пользователе."""
