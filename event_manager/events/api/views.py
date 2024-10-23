from rest_framework import generics

# from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiExample
from .serializers import CategorySerializer, EventSerializer
from .permissions import IsAdminuserOrReadOnly
from events.models import Category, Event


@extend_schema(description="bl ablub text")
class EventListCreateView(generics.ListCreateAPIView):
    """View zum Anlegen und Auflisten von Events."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminuserOrReadOnly]
    # authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        """Den Author hinzufügen."""
        author = self.request.user
        serializer.save(author=author)


class CategoryListCreateView(generics.ListCreateAPIView):
    # da im Inline-Serializer StringRelatedField() genutzt wird,
    # ist es besser, die User-Daten gleich vorzuladen
    queryset = Category.objects.prefetch_related("events__author")
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
