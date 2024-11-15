from sqlalchemy import Column, ForeignKey, Integer, Text, CheckConstraint

from app.core.db import Base


class Donation(Base):
    """Модель представляющая запись о пожертвовании пользователя."""

    __tablename__ = 'donation'

    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
    full_amount = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('full_amount > 0',
                        name='check_donation_amount_positive'),
        CheckConstraint('full_amount >= invested_amount',
                        name='check_donation_invested_amount_not_exceed_full'),
        CheckConstraint('invested_amount >= 0',
                        name='check_donation_invested_amount_positive'),)

    def __repr__(self):
        return (f'(<Donation(id={self.id}, user_id={self.user_id},'
                f'full_amount={self.full_amount},'
                f'invested_amount={self.invested_amount},'
                f'fully_invested={self.fully_invested},'
                f'create_date={self.create_date},'
                f'close_date={self.close_date})>)')
