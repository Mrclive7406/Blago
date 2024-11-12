from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

AUTH_NAME = 'auth'
USERS_NAME = 'users'
AUTH = '/auth'
AUTH_JWT = '/auth/jwt'
USERS_PREFIX = '/users'
USERS_DELETE = '/users/{id}'
MESSAGE_DELETE_USERS = 'Удаление пользователей запрещено!'

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=AUTH_JWT,
    tags=[AUTH_NAME],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix=AUTH,
    tags=[AUTH_NAME],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix=USERS_PREFIX,
    tags=[USERS_NAME]
)


@router.delete(
    USERS_DELETE,
    tags=[USERS_NAME],
    deprecated=True
)
def delete_user(id: str):
    raise HTTPException(
        status_code=HTTPStatus.METHOD_NOT_ALLOWED,
        detail=MESSAGE_DELETE_USERS
    )
