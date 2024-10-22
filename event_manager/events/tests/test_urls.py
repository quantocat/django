"""
Modul für das Testen von GET-Requests
"""
from http import HTTPStatus
from django.utils import timezone
from datetime import timedelta
from django.test import Client, TestCase
from django.urls import reverse 
from django.contrib.auth import get_user_model
from events.models import Category, Event

User = get_user_model()

class CategoryUrlTests(TestCase):

    def setUp(self):
        """Setup Funktion für jeden Test."""
        self.client = Client()  # User Agent
        self.category = Category.objects.create(name="Test Category")

    def test_categories_overview_public(self):
        """Testen, ob die Kategorien-Übersicht öffentlich ist."""
        url = reverse("events:categories")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, text="Übersicht der Kategorien")
        self.assertTemplateUsed(response, "events/categories.html")

    def test_category_detail_public(self):
        url = reverse("events:category", args=(self.category.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, text=self.category.name)
        self.assertTemplateUsed(response, "events/category.html")


class EventUrlTests(TestCase):

    @classmethod
    def setUpClass(cls):
        """Wird einmalig in der Test-Klasse aufgerufen."""
        super(EventUrlTests, cls).setUpClass()
        cls.user = User.objects.create_user(username="Bob", password="abc")
        cls.admin = User.objects.create_superuser(username="Alice", password="abc")

    def setUp(self):
        """Setup Funktion für jeden Test."""
        self.client = Client()  # User Agent
        self.category = Category.objects.create(name="Test Category")
        self.event = Event.objects.create(name="Test Event", 
                                          author=self.user, 
                                          category=self.category,
                                          date=timezone.now() + timedelta(days=2),
                                          min_group=10
                                          )
        
    def test_events_overview_is_login_protected(self):
        """Prüfen, ob die Übersicht der Events login_required ist."""
        url = reverse("events:events")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND) # 302
        self.assertRedirects(response, "/accounts/login/?next=/events/")

        # User einloggen (da Login Required)
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK) # 200
        self.assertTemplateUsed(response, "events/event_list.html")
        self.assertContains(response, text="Test Event")


