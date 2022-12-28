from django.core.management.base import BaseCommand
from users.factories import (
    UserFactory
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        for _ in range(1, 1000):
            UserFactory()
