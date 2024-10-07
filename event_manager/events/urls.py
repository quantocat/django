"""
Events URLs

http://127.0.0.1:8000/events/hello
"""
from django.urls import path 
from .views import hello_world

urlpatterns = [
    path("hello", hello_world, name="hello_world"),
]