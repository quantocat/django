"""
Unit-Testing des Models
"""
from http import HTTPStatus
from django.utils import timezone
from datetime import timedelta
from django.test import Client, TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse 
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from events.models import Category, Event

class EventModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        """Wird einmalig in der Test-Klasse aufgerufen."""
        super(EventModelTest, cls).setUpClass()
        cls.user = get_user_model().objects.create_user(username="Bob", password="abc")
        cls.category = Category.objects.create(name="Test Category")
        cls.date = timezone.now() + timedelta(hours=5)

    def setUp(self):
        self.event = Event.objects.create(name="Test Event", 
                                   category=self.category, 
                                   min_group=2,
                                   author=self.user, 
                                   date=self.date)

    def test_invalid_event_name_raises_error(self):
        """Prüfen, ob ein invalider Name einen Fehler erhebt."""
        self.event.name = "a"
        self.assertRaises(ValidationError, self.event.full_clean)
