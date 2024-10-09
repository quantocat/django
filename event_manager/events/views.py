import logging
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest, Http404
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Category, Event
from .forms import CategoryForm, EventForm

logger = logging.getLogger("django")


class EventDeleteView(SuccessMessageMixin, DeleteView):
    """
    events/3/delete
    """

    model = Event
    success_url = reverse_lazy("events:events")
    success_message = "Event wurde erfolgreich gelöscht"
    # Modelname_confirm_delete.html


class EventUpdateView(SuccessMessageMixin, UpdateView):
    """
    /events/3/update
    """

    model = Event
    form_class = EventForm
    success_message = "Event wurde erfolgreich editiert."


class EventCreateView(SuccessMessageMixin, CreateView):
    """Nach erfolgreicher Erstellung wird an die Addresse von
    obj.get_absolute_url() weitergeleitet (siehe events/models.py)

    /events/create
    """

    model = Event
    form_class = EventForm
    success_message = "Event wurde erfolgreich angelegt."
    # event_form.html

    def form_valid(self, form):
        """Wird aufgerufen, wenn Formular valdide."""
        # print(
        #     "message: ", form.cleaned_data["message"]
        # )  # Zugriff auf Formulardaten ohne Model
        form.instance.author = self.request.user
        logger.info("Es wurde der Author hinzugefügt.")
        return super().form_valid(form)


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
    /events/categories?x=3
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
