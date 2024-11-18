from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud


async def invest_in_entity(session: AsyncSession, entity,
                           balance_entity, amount_to_invest):
    """Инвестирует указанную сумму в сущность и обновляет ее статус."""
    entity.invested_amount += amount_to_invest

    if balance_entity <= amount_to_invest:
        entity.fully_invested = True
        entity.close_date = datetime.now()


async def investing(session: AsyncSession, obj):
    """Осуществляет инвестиции в открытые проекты и пожертвования."""
    project = await charity_project_crud.get_not_fully_invested(session)
    donation = await donation_crud.get_not_fully_invested(session)

    if not project or not donation:
        await session.commit()
        await session.refresh(obj)
        return obj

    balance_project = project.full_amount - project.invested_amount
    balance_donation = donation.full_amount - donation.invested_amount
    amount_to_invest = min(balance_project, balance_donation)

    await invest_in_entity(session, project, balance_project, amount_to_invest)
    await invest_in_entity(session, donation, balance_donation,
                           amount_to_invest)

    await session.commit()
    await session.refresh(project)
    await session.refresh(donation)
    await investing(session, obj)

    return obj