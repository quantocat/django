"""
Events URLs

http://127.0.0.1:8000/events/hello
"""

from django.urls import path
from . import views

app_name = "events"  # immer anlegen, ist der Name der app
# events:category

urlpatterns = [
    path("hello", views.hello_world, name="hello_world"),
    path("categories", views.categories, name="categories"),
    # events/category/3
    path("category/<int:pk>", views.category, name="category"),
    # events/category
    path("category", views.category_create, name="category_create"),
    path("category/<int:pk>/update", views.category_update, name="category_update"),
    # events/
    # .as_view() immer bei klassenbasierten Views (erzeugt Einstiegs-Funktion)
    path("", views.EventListView.as_view(), name="events"),
    path("<int:pk>", views.EventDetailView.as_view(), name="event"),  # /events/3
    # /events/create
    path("create", views.EventCreateView.as_view(), name="event_create"),
    # /events/3/update
    path("<int:pk>/update", views.EventUpdateView.as_view(), name="event_update"),
    # /events/3/delete
    path("<int:pk>/delete", views.EventDeleteView.as_view(), name="event_delete"),
]
