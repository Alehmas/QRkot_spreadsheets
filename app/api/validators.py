from http import HTTPStatus
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud
from app.models import CharityProject
from app.schemas import CharityProjectUpdate


async def check_name_dublicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    """Checking the uniqueness of the project name."""
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name, session)
    if project_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='The project with that name already exists!',
        )


async def check_charity_project_exists(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    """Checking if the project is in the database by ID."""
    charity_project = await charity_project_crud.get_charity_project_by_id(
        project_id, session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Project not found!'
        )
    return charity_project


async def check_charity_project_full(
        project: CharityProject,
) -> None:
    """Checking whether the project is closed
    (whether the required amount has been collected)."""
    if project.fully_invested == 1:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='A closed project cannot be edited!'
        )


async def check_charity_project_full_del(
        project: CharityProject,
) -> None:
    """Checking if the project is closed or if funds have
    been contributed to it."""
    if project.fully_invested == 1 or project.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Funds contributed to the project, can`t be removed!'
        )


async def check_invested_sum(
        project: CharityProject,
        obj_in: CharityProjectUpdate,
) -> None:
    """Amount requested must be greater than deposited."""
    if obj_in.full_amount and project.invested_amount > obj_in.full_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='The requested amount must be greater than the deposited!'
        )
