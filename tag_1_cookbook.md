# Wichtigste Erkenntnisse Tag 1

## Wie erstelle ich ein Projekt?

1. Virtuelles Environment anlegen

    python -m venv env

2. Django installieren

    pip install django

3. Projekt erstellen

    django-admin startproject event_manager


## wie erstelle ich eine App?

1. App erstellen

    python manage.py startapp events

2. App in settings registrieren

settings.py bearbeiten und app den INSTALLED_APPS hinzufügen

    INSTALLED_APPS = [
        [..]
        'django.contrib.staticfiles',
        'events', # <= hinzufügen
    ]

## Wie erstelle ich ein Model in der app events?

1. Model erstellen

events/models.py bearbeiten und Model anlegen

    class Category(models.Model):
        name = models.CharField(max_length=100, unique=True)
        description = models.TextField(null=True, blank=True)

        def __str__(self) -> str:
            return self.name

2. Migrationsdatei erstellen

    python manage.py makemigrations events

3. Migration durchführen

    python manage.py migrate events


## Wie erstelle ich einen neuen Admin-User?

    python manage.py createsuperuser

## Wie mache ich das model in der Admin-Oberfläche verfügbar

events/admin.py bearbeiten

    from django.contrib import admin
    from .models import Category

    @admin.register(Category)
    class CategoryAdmin(admin.ModelAdmin):
        pass

## Wie starte ich den Runserver?

    python manage.py runserver