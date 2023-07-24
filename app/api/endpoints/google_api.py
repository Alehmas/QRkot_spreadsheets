from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.services.google_api import (spreadsheets_create,
                                     spreadsheets_update_value,
                                     set_user_permissions)

router = APIRouter()


@router.get(
    '/',
    response_model=list(),
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)

):
    """Only for superusers. Create a report for projects in a Google sheets."""
    char_project = await charity_project_crud.get_projects_by_completion_rate(
        session
    )
    spreadsheet_id = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheet_id, wrapper_services)
    await spreadsheets_update_value(spreadsheet_id,
                                    char_project,
                                    wrapper_services)
    return char_project
