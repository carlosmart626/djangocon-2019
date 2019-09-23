from django.db.models import Prefetch
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from events.models import Event
from promoters.models import PromoterSpace
from tickets.filters import TicketFilterSet
from .models import Ticket
from .serializers import TicketSerializer, MyTicketsSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = TicketFilterSet
    ordering_fields = (
        'event__name', 'event_start_datetime', )

    def get_queryset(self):
        return Ticket.objects.all() \
            .prefetch_related('user') \
            .prefetch_related(
                Prefetch(
                    'event',
                    queryset=Event.objects.all().only('id', 'name', 'start_datetime', 'end_datetime', 'space').cache()
                )
            ) \
            .prefetch_related(
                Prefetch(
                    'event__space',
                    queryset=PromoterSpace.objects.all().only('id', 'name', 'description').cache()
                )
            ).cache()


class MyTicketsView(APIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        tickets = Ticket.objects.filter(user=user).cache()
        return Response(MyTicketsSerializer({'user': user, 'tickets': tickets}).data)
