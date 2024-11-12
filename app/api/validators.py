from http import HTTPStatus

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models.charity_project import CharityProject

PROJECT_NAME_ALREDY_EXIST = 'Проект с таким именем уже существует!'
NAME_CANNOT_NONE = 'Поле с таким именем не может существовать'
DISCRIPTION_CANNOT_NONE = 'Поле с таким описания не может существовать'
PROJECT_NAME_ALREDY_EXIST = 'Проект с таким именем уже существует!'
PROJECT_NOT_FOUND = 'Проект не найден'
PROJECT_CANNOT_DELETION = ('В проект были внесены средства,'
                           'не подлежит удалению!')
CANNOT_EDITED = 'Закрытый проект нельзя редактировать!'
LESS_AMOUNT_EDITING = ('При редактировании проекта нельзя устанавливать'
                       'требуемую сумму меньше внесённой.')


async def validate_charity_project(
    name: str,
    description: str,
    session: AsyncSession
) -> None:
    if not name:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=NAME_CANNOT_NONE
        )

    if not description:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=DISCRIPTION_CANNOT_NONE
        )

    project_id = await charity_project_crud.get_project_id_by_name(
        name, session)
    if project_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=PROJECT_NAME_ALREDY_EXIST
        )


async def check_name_is_unique(
        charity_project: str,
        session: AsyncSession,
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(
        charity_project, session)
    if project_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=PROJECT_NAME_ALREDY_EXIST
        )


async def check_charity_project_exists(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        object_id=project_id, session=session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=PROJECT_NOT_FOUND
        )
    return charity_project


async def check_project_before_delete(
        project_id,
        session: AsyncSession
):
    charity_project = await charity_project_crud.get(project_id, session)
    if not charity_project:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail=PROJECT_NOT_FOUND
        )
    if charity_project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=PROJECT_CANNOT_DELETION
        )
    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=PROJECT_CANNOT_DELETION
        )
    return charity_project


async def validate_project_update(
    project_id: int,
    full_amount: float,
    session: AsyncSession
):
    charity_project = await charity_project_crud.get(project_id, session)

    if charity_project.fully_invested:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=CANNOT_EDITED
        )

    if full_amount and full_amount < charity_project.invested_amount:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=LESS_AMOUNT_EDITING
        )

    return charity_project
