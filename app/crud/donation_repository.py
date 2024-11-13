from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation


class BaseDonationRepository(CRUDBase):
    model = Donation

    async def get_open_donation(
        self,
        session: AsyncSession
    ):
        donation_result = await session.execute(
            select(Donation)
            .where(Donation.fully_invested == 0)
            .order_by(Donation.create_date)
        )
        return donation_result.scalars().first()


donation_repository_crud = BaseDonationRepository(CRUDBase)
