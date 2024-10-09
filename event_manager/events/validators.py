from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta


def digit_only(value):
    if all(c.isdigit() for c in value):
        raise ValidationError("Wert darf nicht nur aus Zahlen bestehen.")


def bad_word_filter(bad_word_list, current_field_value):
    for bad_word in bad_word_list:
        if bad_word in current_field_value:
            raise ValidationError("Du hast ein verbotenes Wort genutzt")


def date_in_future(current_field_value) -> None:
    if current_field_value < timezone.now() + timedelta(hours=1):
        raise ValidationError(
            "Der Termin muss mindesten 1 Stunde in der Zukunft liegen."
        )
