from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from events.models import Event
from promoters.models import PromoterSpace
from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Ticket.objects.all() \
            .select_related('user') \
            .prefetch_related(
                Prefetch(
                    'event',
                    queryset=Event.objects.all().only('id', 'name', 'start_datetime', 'end_datetime', 'space')
                )
            ) \
            .prefetch_related(
                Prefetch(
                    'event__space',
                    queryset=PromoterSpace.objects.all().only('id', 'name', 'description')
                )
            )
