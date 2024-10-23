""" 
Serializer: Umwandeln von JSON -> Python(Django) und umgekehrt

127.0.0.1:8000/api/events/categories
"""
from rest_framework import serializers
from events.models import Category, Event


class EventSerializer(serializers.ModelSerializer):
    """Serializer für das Event-Model."""

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = "__all__"
        # exclude = ("author",)


class EventInlineSerializer(serializers.ModelSerializer):
    """Inline-Serializer für die Verwendung in Category-Serializer."""

    # löst die ID auf und erzeugt String.
    author = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ("id", "name", "author")


class CategorySerializer(serializers.ModelSerializer):
    """Serializer für das Category-Model."""

    events = EventInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"