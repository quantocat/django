# Projektbeschreibung
- Übungsprojekt Event-Manager im Rahmen des 5-Tages Django-Trainings
- Dozent: Bernd Fischer

## Dependency Managment mit piptools
    python -m venv env
    ./env/Scripts/activate
    pip install pip-tools
    pip-sync requirements.txt requirements-dev.txt

## requirments-txt Dateien erstellen
Dependencies werden ausschließilch in den requirements.in-Dateien festgelegt

    pip-compile requirements.in
    pip-compile requirements-dev.in 

## Umgebungsvariablen festlegen
env_example umbenennen in .env

## Website
- https://ccbv.co.uk/
- https://docs.djangoproject.com/en/5.1/intro/tutorial01/  (Django Tutorial durchführen)
- https://yopad.eu/p/django


## VS-Code Extensions für Django
- Python
- Django (Baptiste Dartheney)

## Tools für Api-Entwicklung
[-Silk](https://github.com/jazzband/django-silk)
[-Locust]https://locust.io/

## Tutorial für Einrichten von Docker, Nginx, Django, Gunicorn

https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

## Ldap
https://medium.com/@itsayushbansal/ldap-authentication-with-django-a2b4f00c9a04
https://django-auth-ldap.readthedocs.io/en/latest/

