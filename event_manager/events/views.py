from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def hello_world(request: HttpRequest) -> HttpResponse:
    """
    View: 
    - hat Parameter request objekt
    - gibt ein HTTP-Response-Objekt zurück
    """
    print(f"{request.method=}")
    print(f"{request.GET=}")
    print(f"{request.user=}")
    print(request.headers)
    return HttpResponse("<b>hallo</b> gfu")
