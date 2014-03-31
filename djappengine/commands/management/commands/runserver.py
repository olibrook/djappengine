from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Disabled runserver command for App Engine applications'

    def handle(self, *args, **options):
        raise CommandError('Use dev_appserver to run App Engine applications')
