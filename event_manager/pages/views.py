from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from events.models import Category


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
