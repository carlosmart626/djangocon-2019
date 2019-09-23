from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from tickets.tests.factories import TicketFactory


class Command(BaseCommand):
    help = 'Creates user and populates db with a few objects for testing'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Process startes'))

        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="admin@admin.co",
            password="123admin123"
        )
        self.stdout.write(self.style.SUCCESS('User created'))

        TicketFactory.create_batch(5)
        TicketFactory.create_batch(5, user=admin_user)
        self.stdout.write(self.style.SUCCESS('Tickets successfully created'))
