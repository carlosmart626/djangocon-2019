from django.core.management.base import BaseCommand

from tickets.tests.factories import TicketFactory


class Command(BaseCommand):
    help = 'Creates creates Tickets for testing'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Process started'))
        count = options['count'][0]
        TicketFactory.create_batch(count)
        self.stdout.write(self.style.SUCCESS('Tickets successfully created'))
