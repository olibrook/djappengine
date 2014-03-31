from django.core.management.base import BaseCommand
from django.utils import crypto


class Command(BaseCommand):
    help = 'Generates a SECRET_KEY for a Django application'

    def handle(self, *args, **options):
        self.stdout.write(
            crypto.get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') + '\n')
