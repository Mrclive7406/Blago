from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import DonationCreate, DonationDB, DonationGet
from app.services.investing import investing

DONATION = '/'
DONATION_MY = '/my'

router = APIRouter()


@router.post(
    DONATION,
    response_model=DonationGet,
    response_model_exclude_none=True,
    summary='Создание благотворительного проета'
)
async def creating_donation(
        donation: DonationCreate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Создает благотворительное пожертвование от имени пользователя."""
    new_donation = await donation_crud.create(donation, session)
    return await investing(session, new_donation)


@router.get(
    DONATION,
    response_model=list[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
    summary='Полчение всех благотворительных проектов'
)
async def get_all_donation(
        session: AsyncSession = Depends(get_async_session)
) -> list[str]:
    """Полчение всех благотворительных проектов."""
    return await donation_crud.get_multi(session)


@router.get(
    DONATION_MY,
    response_model=list[DonationGet],
    summary='Получение вашего благотворительного проекта'
)
async def get_my_donation(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
) -> list[str]:
    """Получает список пожертвований, сделанных текущим пользователем."""
    return await donation_crud.get_by_user(
        session, user
    )
