"""
PROJEKT URLS

admin2 token: b924fca2063f615acdc17759ee464e814adda815
"""

from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("api/token", obtain_auth_token, name="token"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # api/events/categories
    path("api/events/", include("events.api.urls")),
    # path("api/", include("pages.api.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include("pages.urls")),  # http://127.0.0.1:8000
    path("admin/", admin.site.urls),  # http://127.0.0.1:8000/admin
    path("events/", include("events.urls")),  # http://127.0.0.1:8000/events/*

    path(
        "schema/",
        SpectacularAPIView.as_view(api_version="v1"),
        name="schema",
    ),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),  # aus schema/
        name="swagger-ui",
    ),


] + debug_toolbar_urls()
