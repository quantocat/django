# Wichtigste Erkenntnisse Tag 3

## Formulare erstellen (funktionsbasiert)

1) Formular erstellen (auf Basis von Model)

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = "__all__"


2) View erstellen (Klassenbasiert)

    class EventCreateView(SuccessMessageMixin, CreateView):
        """Nach erfolgreicher Erstellung wird an die Addresse von
        obj.get_absolute_url() weitergeleitet (siehe events/models.py)

        /events/create
        """

        model = Event
        form_class = EventForm

3) Template erstellen

in events/templates ein Form-Template erstellen

- Model Event
- CreateView => event_form.html
- UpdateView => event_form.html

um das Formular schöner anzuzeigen, crispyforms nutzen, siehe:

https://djangoheroes.spielprinzip.com/working_with_forms/working_with_forms.html#crispy-forms

4) Url festlegen

events/urls.py bearbeiten

    # /events/create
    path("create", views.EventCreateView.as_view(), name="event_create"),

    # /events/3/update
    path("<int:pk>/update", views.EventUpdateView.as_view(), name="event_update"),


## statische Dateien ausliefern

Um statische Dateien auch im Produktiv-Betrieb über Django ausliefern zu können,
bietet sich das Drittanbieter-Modul whitenoise an.

    https://djangoheroes.spielprinzip.com/profiwissen/whitenoise.html