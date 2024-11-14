from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


class CRUDBase:
    """Базовый репозиторий для работы с моделями."""

    def __init__(self, model):
        """Инициализирует CRUDBase с заданной моделью."""
        self.model = model

    async def get(
            self,
            object_id: int,
            session: AsyncSession,
    ):
        """Возвращает объект по его идентификатору."""
        db_object = await session.execute(
            select(self.model).where(self.model.id == object_id)
        )
        return db_object.scalars().first()

    async def get_multi(
            self,
            session: AsyncSession
    ):
        """Возвращает список всех объектов модели."""
        db_objects = await session.execute(select(self.model))
        return db_objects.scalars().all()

    async def create(
            self,
            object_in,
            session: AsyncSession,
    ):
        """Создает новый объект модели."""
        object_in_data = object_in.dict()
        db_object = self.model(**object_in_data)
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def update(
            self,
            db_object,
            object_in,
            session: AsyncSession,
    ):
        """Обновляет существующий объект модели."""
        object_data = jsonable_encoder(db_object)
        update_data = object_in.dict(exclude_unset=True)
        for field in object_data:
            if field in update_data:
                setattr(db_object, field, update_data[field])
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def remove(
            self,
            db_object,
            session: AsyncSession,
    ):
        """Удаляет существующий объект модели."""
        await session.delete(db_object)
        await session.commit()
        return db_object


class CharityProjectRepository(CRUDBase):
    """Репозиторий для управления благотворительными проектами."""

    def __init__(self):
        """Инициализирует CharityProjectRepository с заданной моделью."""
        super().__init__(CharityProject)

    async def get_open_project(self, session: AsyncSession):
        """Возвращает первый открытый благотворительный проект."""
        project_result = await session.execute(
            select(CharityProject)
            .where(CharityProject.fully_invested == 0)
            .order_by(CharityProject.create_date)
        )
        return project_result.scalars().first()


class DonationRepository(CRUDBase):
    """Репозиторий для управления пожертвованиями."""

    def __init__(self):
        """Инициализирует DonationRepository с заданной моделью."""
        super().__init__(Donation)

    async def get_open_donation(self, session: AsyncSession):
        """Возвращает первое открытое пожертвование."""
        donation_result = await session.execute(
            select(Donation)
            .where(Donation.fully_invested == 0)
            .order_by(Donation.create_date)
        )
        return donation_result.scalars().first()


charity_project_repository_crud = CharityProjectRepository()
donation_repository_crud = DonationRepository()
base_repository_crud = CRUDBase