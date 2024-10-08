# Wichtigste Erkenntnisse Tag 2

## Funktionsbasierte Views anlegen Detail

1. urls.py bearbeiten

Platzhalter für ID definieren. Dieser Platzhalter (pk) steht später
in der View zur Verfügung.

    path("category/<int:pk>", views.category, name="category")

2. views.py bearbeiten

Im Parameterkopf der Funktion die Platzhalter-Variable pk definieren.
mit ihrer Hilfe das Objekt aus der Datenbank laden.
Oder im Fall eines Nichtvorhandenseins einen 404-Fehler auslösen.

    def category(request, pk):
    """
    events/category/3
    """
    category = get_object_or_404(Category, pk=pk)

    return render(request, "events/category.html", {"category": category})

3. Templates

    Alle Templates sollten in einem Sub-Verzeichnis von Templates abgelegt 
    werden. Dieses Verzeichnis trägt meistens den gleichen Namen wie die App (events).


## Funktionsbasierte Views anlegen (list)

1. urls.py bearbeiten
Hier ist kein Platzhalter nötig

    path("categories", views.categories, name="categories"),

2. View erstellen (views.py)

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

## Klassenbasierte generische Views

Hierbei handelt es sich um Views, die für Standard-Aufgaben optimiert wurden. 
Alle Funktioalitäten lassen sich über Variablen und Methoden überschreiben.

1. urls.py bearbeiten
das zweite Argument von path ist ein Funktionsobjekt, welches durch den Aufruf der Methode
as_view() der klassenbasierten View erstellt wird. 

    path("events", views.EventListView.as_view(), name="events"),

2. views.py bearbeiten
Im einfachsten Fall ist die Listview wie folgt definiert. 
Das Template einer generischen klassenbasierten LIstView ist immer
MODELNAME-LOWERCASE_list (zb. event_list.html)

    class EventListView(ListView):
        model = Event

## Django-Debug-Toolbar

Um zu überprüfen, welche Datenbankabfragen stattfinden, lässt sich die Django-Debug-toolbar nutzen.

https://django-debug-toolbar.readthedocs.io/en/latest/