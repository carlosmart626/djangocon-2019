from url_filter.filtersets import ModelFilterSet
from .models import Ticket


class TicketFilterSet(ModelFilterSet):

    class Meta:
        model = Ticket
        fields = (
            'id',
            'event',
            'user',
            'already_used',
        )
