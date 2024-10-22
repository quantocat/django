"""
Modul für das Testen von POSt-Request (via forms)
"""
from http import HTTPStatus
from django.utils import timezone
from datetime import timedelta
from django.test import Client, TestCase
from django.urls import reverse 
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from events.models import Category, Event


def show_form_errors(response) -> None:
    """Show Form Errors from response context."""

    if "form" in response.context:
        form = response.context["form"]

        # Check if the form has errors
        if form.errors:
            print("Form Errors:", form.errors)

            # For a more detailed output, iterate through the errors
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in field '{field}': {error}")
        else:
            print("No form errors found.")
    else:
        print("Form is not in the context.")


class EventFormTests(TestCase):

    @classmethod
    def setUpClass(cls):
        """Wird einmalig in der Test-Klasse aufgerufen."""
        super(EventFormTests, cls).setUpClass()
        cls.user = get_user_model().objects.create_user(username="Bob", password="abc")


    def setUp(self):
        """Setup Funktion für jeden Test."""
        self.client = Client()  # User Agent
        self.category = Category.objects.create(name="Test Category")
        self.valid_payload = {
            "name": "Testevent",
            "category": self.category.pk,
            "date": timezone.now() + timedelta(hours=5),
            "sub_title": "valid subtitle",
            "min_group": 2
        }
    
    def test_create_event_successfully(self):
        """Prüfen, ob ein Event erfolgreich erstellt wurde."""
        self.client.force_login(self.user)
        url = reverse("events:event_create")

        # GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)   # 200
        self.assertTemplateUsed(response, "events/event_form.html")

        # POST
        response = self.client.post(url, self.valid_payload)
        # show_form_errors(response)
        # Aufgabe: 3 Asserts
        # 1. Ist Statuscode 302
        # 2. Stimmt Redirect (get_absolute_url nutzen)
        # 3. Prüfen, ob es eingetragen wurde
        
        # show_form_errors(response)
        testObject = Event.objects.all()[0]
        redir_url = testObject.get_absolute_url()
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redir_url)
        self.assertEqual(testObject.name, self.valid_payload["name"])
        # self.assertEqual(model_to_dict(testObject, exclude=["author", "id"]), self.valid_payload)
        # payload = model_to_dict(testObject, exclude=["author", "id"])
        
