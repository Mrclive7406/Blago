from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_charity_project_exists,
                                check_name_is_unique,
                                check_project_before_delete,
                                validate_charity_project,
                                validate_project_update)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.services.investing import investing

CHARITY_PROJECT_PATH = '/'
CHARITY_PROJECT_MODIFY_PATH = '/{project_id}'
CREATE_PROJECT = 'Создание благотворительного проекта'
GET_ALL_PROJECT = 'Получение всех благотворительных проектов'
UPDATE_PROJECT = 'Обновление благотворительного проекта'
DELETE_PROJECT = 'Удаление благотворительного проекта'

router = APIRouter()


@router.post(
    CHARITY_PROJECT_PATH,
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
    summary=CREATE_PROJECT,
)
async def create_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    await validate_charity_project(
        name=charity_project.name,
        description=charity_project.description,
        session=session
    )

    return await investing(
        session,
        await charity_project_crud.create(charity_project, session))


@router.get(
    CHARITY_PROJECT_PATH,
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
    summary=GET_ALL_PROJECT,
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    return await charity_project_crud.get_multi(session)


@router.patch(
    CHARITY_PROJECT_MODIFY_PATH,
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    summary=UPDATE_PROJECT,
)
async def update_charity_project(
        project_id: int,
        object_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    project = await validate_project_update(
        project_id=project_id,
        full_amount=object_in.full_amount,
        session=session
    )

    if object_in.name:
        await check_name_is_unique(object_in.name, session)

    return await charity_project_crud.update(project, object_in, session)


@router.delete(
    CHARITY_PROJECT_MODIFY_PATH,
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    summary=DELETE_PROJECT,
)
async def remove_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),):

    await check_project_before_delete(project_id, session)
    charity_project = await check_charity_project_exists(
        project_id, session)

    return await charity_project_crud.remove(
        charity_project, session)
