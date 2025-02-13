from datetime import datetime
from typing import AsyncGenerator

from sqlalchemy import Boolean, Column, DateTime, Integer, func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:
    """Генерирует имя таблицы на основании имени класса в нижнем регистре."""

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: int = Column(Integer, primary_key=True)
    invested_amount: int = Column(Integer, default=0)
    fully_invested: bool = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime, default=func.now(), nullable=True)


Base = declarative_base(cls=PreBase)
engine = create_async_engine(settings.database_url)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Создает асинхронную сессию для работы с базой данных."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
