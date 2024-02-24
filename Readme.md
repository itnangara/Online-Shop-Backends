# Postgres
    CREATE DATABASE Kidszonesa;

# Dependencies
    pip install django-cors-headers
    python -m pip install --upgrade pip
    pip install djangorestframework
    pip install psycopg2

# Running the django project
    cd 'C:\Users\nanga\Desktop\All Folders\Projects\Online Shop\Online-Shop-Backends'
    (Terminal session 1): venv\Scripts\activate
    (Terminal session 2): cd django_api
        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver

