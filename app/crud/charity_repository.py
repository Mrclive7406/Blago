from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class BaseCharityRepository(CRUDBase):
    model = CharityProject

    async def get_open_project(
        self,
        session: AsyncSession
    ):
        project_result = await session.execute(
            select(CharityProject)
            .where(CharityProject.fully_invested == 0)
            .order_by(CharityProject.create_date)
        )
        return project_result.scalars().first()


charity_repository_crud = BaseCharityRepository(CRUDBase)
