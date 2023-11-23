# Installation (Development)
*This installation requires Python 12 installed locally

- Windows
$ python -m venv .venv
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1
(.venv) $ python -m pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py runserver

- macOS
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python3 -m pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py runserver

# Installation (Testing)
*This installation requires Docker installed locally
** Linux Environment with PostgreSQL Database

- Windows & macOS
$ docker build .
$ docker-compose up

Return to 'http://127.0.0.1:8000/' in your browser
