from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, NonNegativeInt, PositiveInt


class DonationBase(BaseModel):
    """
    Базовая модель для донатного проектов.

    """
    full_amount: PositiveInt = Field()
    comment: Optional[str] = Field()

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    """
    Модель для создания нового донатного проекта.

    """

    class Config:
        extra = Extra.forbid


class DonationGet(DonationBase):
    """
    Модель для запроса существующего донатного проекта.
    """

    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(DonationGet):
    """
    Модель базы данных для донатного проектов.

    """
    user_id: Optional[int]
    invested_amount: NonNegativeInt = Field(0)
    fully_invested: bool = Field(False)
    close_date: Optional[datetime]