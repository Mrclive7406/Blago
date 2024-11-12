from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.services.google_api import (spreadsheets_create, set_user_permissions,
                                     spreadsheets_update_value)
from app.crud import charity_project

router = APIRouter()


@router.post(
    '/google',
    response_model=list,
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        # Сессия
        session: AsyncSession = Depends(get_async_session),
        # «Обёртка»
        wrapper_services: Aiogoogle = Depends(get_service)

):
    project = await charity_project.get_project_by_complection_rate(session)
    spreadsheetid = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheetid, wrapper_services)
    await spreadsheets_update_value(spreadsheetid,
                                    project,
                                    wrapper_services)
    return project
