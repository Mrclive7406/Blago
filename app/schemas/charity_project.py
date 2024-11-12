from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, NonNegativeInt, PositiveInt

from app.core.constants import MAX_LENGTH, MIN_LENGTH


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None,
                                min_length=MIN_LENGTH,
                                max_length=MAX_LENGTH)
    description: Optional[str] = Field(None, min_length=MIN_LENGTH)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(None, min_length=MIN_LENGTH, max_length=MAX_LENGTH)
    description: str = Field(None, min_length=MIN_LENGTH)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: NonNegativeInt = Field(0)
    fully_invested: bool = Field(False)
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True