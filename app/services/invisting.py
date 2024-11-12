from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.donation import donation_crud


async def invisting(session: AsyncSession, obj):
    project = await donation_crud.get_open_project(session)
    donation = await donation_crud.get_open_donation(session)

    if not project or not donation:
        await session.commit()
        await session.refresh(obj)
        return obj

    balance_project = project.full_amount - project.invested_amount
    balance_donation = donation.full_amount - donation.invested_amount
    amount_to_invest = min(balance_project, balance_donation)

    project.invested_amount += amount_to_invest
    donation.invested_amount += amount_to_invest

    if balance_project <= balance_donation:
        project.fully_invested = True
        project.close_date = datetime.now()

    if balance_donation <= balance_project:
        donation.fully_invested = True
        donation.close_date = datetime.now()

    await session.commit()
    await session.refresh(project)
    await session.refresh(donation)
    await invisting(session, obj)
    return obj
