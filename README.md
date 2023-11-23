
# Resources

Metasearcher for databases

## Installation

**Development scenario - Windows Environment & SQLite3**\
_Requires Python 12 installed locally_


Create and activate virtual environment:
```bash
    python -m venv .venv
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    .venv\Scripts\Activate.ps1

```
Install requirements and initialize server:
```bash
    (.venv) python -m pip install -r requirements.txt
    (.venv) python manage.py migrate
    (.venv) python manage.py createsuperuser
    (.venv) python manage.py runserver
```

**Testing scenario - Linux Environment & PostgreSQL**\
_Requires Docker installed locally_


Build up Docker Container
```bash
    docker build .
    docker-compose up
```
Initialize server:
```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
```
