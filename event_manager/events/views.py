from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import ListView, DetailView
from .models import Category, Event
from .forms import CategoryForm


class EventDetailView(DetailView):
    model = Event
    # event_detail.html


class EventListView(ListView):
    model = Event
    queryset = Event.objects.select_related("category", "author").all()
    # generische Name events/event_list.html
    # https://127.0.0.1:8000/events?search=eiu

    # event_detail.html

    # /events/?search=suchanfrage
    def get_queryset(self):
        suchanfrage = self.request.GET.get("search")
        if suchanfrage:
            return super().get_queryset().filter(name__contains=suchanfrage)
        return super().get_queryset()


def category_update(request, pk):
    """
    GET & POST: events/3/update
    """
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect("events:categories")

    return render(
        request,
        "events/category_form.html",
        {"form": form},
    )


def category_create(request):
    """
    GET & POST: events/create
    """
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect("events:categories")
    else:
        form = CategoryForm()

    return render(
        request,
        "events/category_form.html",
        {"form": form},
    )


def category(request, pk):
    """
    events/category/3
    """
    # try:
    #     category = Category.objects.get(pk=pk)
    # except Category.DoesNotExist:
    #     raise Http404("Diese Category ist nicht vorhanden.")

    # shortcut für den try-except-Block
    category = get_object_or_404(Category, pk=pk)

    return render(request, "events/category.html", {"category": category})


def categories(request) -> HttpResponse:
    """
    /events/categories
    """
    categories = Category.objects.all()  # categories[0].name
    return render(
        request,
        "events/categories.html",
        {
            "categories": categories,
        },
    )


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
