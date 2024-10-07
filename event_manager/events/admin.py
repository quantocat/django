from django.contrib import admin
from .models import Category, Event


class EventInlineAdmin(admin.TabularInline):
    """nur dafür da, um auf der Category-Detailseite gezeigt zu werden."""

    model = Event
    fields = ("name", "date")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    def number_events(self, obj):
        # obj ist jedes Kategorie-Objekt
        return obj.events.count()  # obj.events => Related manager

    list_display = (
        "id",
        "name",
        "number_events",
    )

    inlines = [EventInlineAdmin]  # wird als Inline-Admin angezeigt


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    search_fields = ("name", "sub_title")  # Suchbox wird erstellt

    list_display = (
        "id",
        "name",
        "category",
    )
    list_display_links = (
        "id",
        "name",
    )
