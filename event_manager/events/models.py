from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()  # aktuelles User-Model


class DateMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Beim Anlegen einmalig sdfasdf asd
    updated_at = models.DateTimeField(auto_now=True)  # beim Updaten Timestamp setzen

    class Meta:
        abstract = True


class Category(DateMixin):
    """Kategorie für einen Event."""

    class Meta:
        ordering = ["name"]  # "-name"
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    name = models.CharField(max_length=100, unique=True)  # VARCHAR 100

    # blank=True => darf im Formular leer sein
    # null=True => darf in der DB null sein (nullable)
    sub_title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Untertitel",
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Event(DateMixin):
    """Eventobjekt mit Datum und User."""

    class GroupSize(models.IntegerChoices):
        BIG = 10
        SMALL = 2

    name = models.CharField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events",  # bob.events.all()
    )
    min_group = models.IntegerField(choices=GroupSize.choices)

    # https://docs.djangoproject.com/en/5.1/ref/models/fields/
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  # was passiert, wenn Kategorie gelöscht wird?
        related_name="events",
    )  # Related Manager. sport.events.all()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
