from datetime import datetime

from aiogoogle import Aiogoogle
from app.core.config import settings

FORMAT = "%Y/%m/%d %H:%M:%S"
NOW_DATE_TIME = datetime.now
ROW_COUNT = 100
COL_COUNT = 11
TABLE_VALUES = [
    ['Отчет от', 'Дата отчета'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
SHEET_TYPE = 'GRID'


async def spreadsheets_body_create(
        sheet_type: str,
        date_now: datetime,
        row_count: int,
        col_count: int) -> dict:
    spreadsheet_body = {
        'properties': {'title': f'Отчет на {date_now().strftime(FORMAT)}',
                       'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': sheet_type,
                                   'sheetId': 0,
                                   'title': 'Лист1',
                                   'gridProperties': {'rowCount': row_count,
                                                      'columnCount': col_count
                                                      }}}]
    }
    return spreadsheet_body


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    """Функция создания таблицы в Google Sheets"""
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = await spreadsheets_body_create(
        SHEET_TYPE, NOW_DATE_TIME, ROW_COUNT, COL_COUNT)
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheet_id = response['spreadsheetId']
    return spreadsheet_id


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    """Функция выдачи прав для работы с документами"""
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        charity_projects: list,
        wrapper_services: Aiogoogle
) -> None:
    """Функция наполнения таблицы в Google Sheets"""
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = TABLE_VALUES.copy()
    table_values[0][1] = NOW_DATE_TIME().strftime(FORMAT)
    for project in charity_projects:
        new_row = [str(project['name']), str(project['time_finish']),
                   str(project['description'])]
        if len(table_values) == ROW_COUNT - 1:
            table_values.append(['Остальные значения не влезли!!!!!!!!!!'])
            break
        table_values.append(new_row)
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range='A1:' + str(chr(ord('A') + COL_COUNT - 1)) + str(ROW_COUNT),
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
