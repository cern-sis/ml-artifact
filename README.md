# ML Artifact

Proof Of Concept for the ML artifact repository

## Development Instructions

- Major Dependency requirements
    1. Python 3
    2. Django 4
    3. Django Rest Framework 3

- Local Setup

    1. `python3 -m venv env`
    2. `source env/bin/activate`
    3. `pip install -r requirements.txt`
    4. `python manage.py runserver`

- Database migrations

    1. `python manage.py makemigrations`
    2. `python manage.py migrate`
