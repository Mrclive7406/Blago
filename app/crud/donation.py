from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):
    """Класс для управления операциями с пожертвованиями."""

    async def get_by_user(
            self,
            session: AsyncSession,
            user: User
    ) -> list[Donation]:
        """Получает все пожертвования, сделанные указанным пользователем."""
        user_donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return user_donations.scalars().all()


donation_crud = CRUDDonation(Donation)
