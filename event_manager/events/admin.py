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

    @admin.display(description="Setze Events aktiv")
    def set_active(self, request, queryset):
        """Setze alle Objekte des Querysets auf aktiv."""
        queryset.update(is_active=True)

    @admin.display(description="Setze Events inaktiv")
    def set_inactive(self, request, queryset):
        """Setze alle Objekte des Querysets auf inaktiv."""
        queryset.update(is_active=False)

    search_fields = ("name", "sub_title")  # Suchbox wird erstellt
    actions = [
        "set_active",
        "set_inactive",
    ]

    list_display = (
        "id",
        "name",
        "category",
        "is_active",
    )
    list_display_links = (
        "id",
        "name",
    )

    fieldsets = (
        ("Standard Infos", {"fields": ("name", "date", "category")}),
        (
            "Detail Infos",
            {"fields": ("description", "min_group", "is_active", "sub_title")},
        ),
    )
