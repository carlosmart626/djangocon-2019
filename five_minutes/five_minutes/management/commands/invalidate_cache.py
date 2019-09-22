from django.core.cache import cache
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Invalidating cache example'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Delete key'))
        cache.delete('event_list*')
        self.stdout.write(self.style.SUCCESS('Delete key successfully'))
