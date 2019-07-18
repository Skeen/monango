"""Command for generating default boards."""
from django.core.management.base import BaseCommand
from engine.fixture import seed_us_board


# pylint: disable=missing-docstring
class Command(BaseCommand):

    def handle(self, *args, **options):
        seed_us_board()
