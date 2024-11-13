from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import Base


class Donation(Base):
    """
    Модель пожертвования, представляющая запись о пожертвовании пользователя.

    """
    __tablename__ = 'donation'

    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
    full_amount = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"(<Donation(id={self.id}, user_id={self.user_id}, "
                f"full_amount={self.full_amount},"
                f"invested_amount={self.invested_amount},  "
                f"fully_invested={self.fully_invested}, "
                f"create_date={self.create_date}, "
                f"close_date={self.close_date})>)")
