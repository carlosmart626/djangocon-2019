from datetime import timedelta

import factory
from django.utils import timezone

from events.models import Event
from promoters.tests.factories import PromoterSpaceFactory


class EventFactory(factory.DjangoModelFactory):

    class Meta:
        model = Event

    name = factory.Sequence(lambda n: "Event %03d" % n)
    start_datetime = timezone.now()
    end_datetime = timezone.now() + timedelta(hours=6)
    space = factory.SubFactory(PromoterSpaceFactory)
    promoter = factory.SelfAttribute('space.promoter')
    description = "#Event description \n\n##Data \n\nDescription body"
