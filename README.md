#  QRKot

##  Description
QRKot is an application for the Charitable Foundation for supporting Cats.

The Foundation collects donations for various targeted projects: for medical care
needy caudates, for the arrangement of a cat colony in the basement, for food for the remaining
without care for cats - for any purpose related to the support of the cat population.

###  Projects
Several target projects can be opened in the QRKot Foundation. Each project
there is a name, description and the amount that is planned to be collected. After
The required amount is collected - the project is closed. Donations to projects come from
the principle of First In, First Out: all donations go to the project opened earlier than others;
when this project collects the required amount and closes, donations begin
enter the next project.

### Donations
Each user can make a donation and accompany it with a comment.
Donations are not targeted: they are made to the fund, and not to a specific project.
Each donation received is automatically added to the first open project, who has not yet collected
the required amount. If the donation is more than the required amount or there are no open projects
in the Fund - the remaining money is waiting for the opening of the next project.
When creating a new project, all uninvested donations are automatically invest in a new project.

### Users
Target projects are created by site administrators.
Any user can see a list of all projects, including required and already contributed amounts.
This applies to all projects, both open and closed.
Registered users can send donations and
view a list of your donations.

The superuser can:
- create projects
- delete projects that have not been funded,
- change the name and description of an existing project, set a new one for it
  the required amount (but not less than the amount already paid).

## Technologies used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/Fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white) ![SQlite](https://img.shields.io/badge/SQLite-003b57?style=for-the-badge&logo=sqlite&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-6d8a7f?style=for-the-badge) ![Google Sheets](https://img.shields.io/static/v1?style=for-the-badge&message=Google+Sheets&color=34A853&logo=Google+Sheets&logoColor=FFFFFF&label=) ![Google Drive](https://img.shields.io/static/v1?style=for-the-badge&message=Google+Drive&color=4285F4&logo=Google+Drive&logoColor=FFFFFF&label=)

## Preparation and launch of the project
**Step 1** Clone the repository on your local machine:
```bash
git clone git@github.com:Alehmas/QRkot_spreadsheets.git
```

**Step 2** Change to a new directory. Initialize and activate the virtual environment
```bash
cd cat_charity_fund/
python -m venv venv
source venv/Scripts/activate
```

**Step 3** Update pip and install project dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Step 4** Add .env file:
```
APP_TITLE=QRKot App
APP_DESCRIPTION=Application for the Cat Charitable Foundation
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=<SECRET>
FIRST_SUPERUSER_EMAIL=<FIRST_SUPERUSER_EMAIL>
FIRST_SUPERUSER_PASSWORD=<FIRST_SUPERUSER_PASSWORD>
EMAIL=<EMAIL>
TYPE=service_account
PROJECT_ID=<PROJECT_ID>
PRIVATE_KEY_ID=<PRIVATE_KEY_ID>
PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\n<PRIVATE_KEY>\n-----END PRIVATE KEY-----\n
CLIENT_EMAIL=<CLIENT_EMAIL>
CLIENT_ID=<CLIENT_ID>
AUTH_URI=<AUTH_URI>
TOKEN_URI=<TOKEN_URI>
AUTH_PROVIDER_X509_CERT_URL=<AUTH_PROVIDER_X509_CERT_URL>
CLIENT_X509_CERT_URL=<CLIENT_X509_CERT_URL>
```

**Step 5** Create and apply migrations as needed
```bash
alembic revision --autogenerate -m "First migration" 
alembic upgrade head
```

**Step 6** Launch the application
```bash
uvicorn app.main:app --reload
```

## Request examples
Examples of requests, access rights, possible answers are available in the link to the projects [documentation](http://127.0.0.1:8000/docs)

## Authors
- [Aleh Maslau](https://github.com/Alehmas)