"""
PROJEKT URLS
"""

from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", include("pages.urls")),  # http://127.0.0.1:8000
    path("admin/", admin.site.urls),  # http://127.0.0.1:8000/admin
    path("events/", include("events.urls")),  # http://127.0.0.1:8000/events/*
] + debug_toolbar_urls()
