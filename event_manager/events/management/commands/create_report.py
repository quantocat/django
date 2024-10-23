"""
eigenes Managmentment Commando erstellen
Management Commando create_report
"""

from django.core.management.base import BaseCommand, CommandParser
from events.models import Event, Category


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.description = "Erstelle einen Report auf Basis von xy"

        parser.add_argument(
            "-m", "--month", type=int, help="Month of report", required=True,
        )

    def handle(self, *args, **kwargs):
        """Einstiegs-Methode in das Kommando."""
        objects = Event.objects.all()
        month = kwargs.get("month")  # Argument von Argumentparser
        print(f"{month=}")

        for obj in objects:
            print(obj)
