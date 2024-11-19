from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import BaseCharityRepository
from app.models import Donation, User


class CRUDDonation(BaseCharityRepository):
    """Класс для управления операциями с пожертвованиями."""

    def __init__(self):
        """Инициализирует DonationRepository с заданной моделью."""
        super().__init__(Donation)

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


donation_crud = CRUDDonation()
