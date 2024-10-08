from django import forms
from .models import Category, Event


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
