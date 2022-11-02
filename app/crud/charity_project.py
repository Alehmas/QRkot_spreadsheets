import operator
from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject
from app.schemas import CharityProjectUpdate


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        """"Функция получения проекта из БД по имени"""
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_charity_project_by_id(
            self,
            project_id: int,
            session: AsyncSession,
    ) -> Optional[CharityProject]:
        """"Функция получения проекта из БД по id"""
        db_project = await session.execute(
            select(CharityProject).where(
                CharityProject.id == project_id
            )
        )
        db_project = db_project.scalars().first()
        return db_project

    async def update_charity_project(
            self,
            db_project: CharityProject,
            project_in: CharityProjectUpdate,
            session: AsyncSession,
    ) -> CharityProject:
        """"Функция обновления проекта в БД"""
        obj_data = jsonable_encoder(db_project)
        update_data = project_in.dict(exclude_unset=True)
        if 'full_amount' in update_data:
            if obj_data['invested_amount'] == update_data['full_amount']:
                update_data['fully_invested '] = True
        for field in obj_data:
            if field in update_data:
                setattr(db_project, field, update_data[field])
        session.add(db_project)
        await session.commit()
        await session.refresh(db_project)
        return db_project

    async def delete_charity_project(
            self,
            db_project: CharityProject,
            session: AsyncSession,
    ) -> CharityProject:
        """"Функция удаления проекта из БД"""
        await session.delete(db_project)
        await session.commit()
        return db_project

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list():
        charity_projects = await session.execute(
            select([CharityProject.name, CharityProject.create_date,
                    CharityProject.close_date,CharityProject.description,]
            ).where(CharityProject.fully_invested)
        )
        charity_projects = charity_projects.all()
        update_projects = []
        for project in charity_projects:
            update_project = dict()
            time_finish = project.close_date - project.create_date
            update_project['name'] = project.name
            update_project['time_finish'] = str(time_finish)
            update_project['description'] = project.description
            update_projects.append(update_project)
        update_projects.sort(key=operator.itemgetter('name'))  #!!!!!!!!!!!!!остановился здесь
        return update_projects

charity_project_crud = CRUDCharityProject(CharityProject)
