from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, NonNegativeInt, PositiveInt

from app.core.constants import MAX_LENGTH, MIN_LENGTH


class CharityProjectBase(BaseModel):
    """Базовая модель для благотворительных проектов."""

    name: Optional[str] = Field(
        None,
        min_length=MIN_LENGTH,
        max_length=MAX_LENGTH
    )
    description: Optional[str] = Field(None, min_length=MIN_LENGTH)
    full_amount: Optional[PositiveInt]

    class Config:
        """Конфигурации для CharityProjectBase."""

        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    """Модель для создания нового благотворительного проекта."""

    name: str = Field(..., min_length=MIN_LENGTH, max_length=MAX_LENGTH)
    description: str = Field(..., min_length=MIN_LENGTH)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    """Модель для обновления существующего благотворительного проекта."""


class CharityProjectDB(CharityProjectBase):
    """Модель базы данных для благотворительных проектов."""

    id: int
    invested_amount: NonNegativeInt = Field(0)
    fully_invested: bool = Field(False)
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        """Конфигурации для CharityProjectDB."""

        orm_mode = True
