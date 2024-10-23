from django.urls import path

from .views import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
    EventListCreateView,
)

urlpatterns = [
    path("", EventListCreateView.as_view(), name="event-list-create"),
    path("category", CategoryListCreateView.as_view(), name="category-list-create"),
    path(
        "category/<int:pk>",
        CategoryRetrieveUpdateDestroyView.as_view(),
        name="category-retrieve-update-destroy",
    ),
]
