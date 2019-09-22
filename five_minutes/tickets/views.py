from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Ticket.objects.all() \
            .select_related('event', 'user') \
            .prefetch_related('event__space')
