from sqlalchemy import Column, Integer, String, Text

from app.core.db import Base


class CharityProject(Base):
    """
    Модель благотворительного проекта.

    """
    __tablename__ = 'charity_project'

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    full_amount = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"<CharityProject(id={self.id}, "
                f"name='{self.name}', "
                f"description='{self.description}', "
                f"full_amount={self.full_amount}, "
                f"invested_amount={self.invested_amount}, "
                f"fully_invested={self.fully_invested}, "
                f"create_date={self.create_date}, "
                f"close_date={self.close_date})>")