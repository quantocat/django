from django import forms
from django.core.exceptions import ValidationError
from .models import Category, Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        exclude = ("author",)

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "datetime-local"},
                format=("%Y-%m-%d %H:%M"),  # iso8601-format
            ),
        }

    def clean_sub_title(self):
        """Clean oder Validierung vornehmen. Rückgabewert dieser Funktion
        ist der neue Subtitle, nach Absenden des Formulars und vor Eintrag in die DB."""
        sub_title = self.cleaned_data["sub_title"]
        illegal_chars = ("*", "-")
        if isinstance(sub_title, str) and sub_title.startswith(illegal_chars):
            raise ValidationError(
                "Der Subtitle darf nicht mit illegalen Zeichen beginnen."
            )
        return sub_title

    def clean(self) -> dict:
        """Clean eigent sich für Crossfield-Validierung (feldübergreifende Validierung)."""
        super().clean()  # ruft die Feld-Validierer auf

        sub_title = self.cleaned_data["sub_title"] or ""
        name = self.cleaned_data["name"] or ""

        if "ab" in sub_title and "ab" in name:
            raise ValidationError("ab in Name und Subtitle geht nicht")

        return self.cleaned_data

    # message = forms.CharField(max_length=200, required=True)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
