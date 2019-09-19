import factory

from events.tests.factories import EventFactory
from tickets.models import Ticket
from users.tests.factories import UserFactory


class TicketFactory(factory.Factory):
    class Meta:
        model = Ticket

    event = factory.SubFactory(EventFactory)
    user = factory.SubFactory(UserFactory)
