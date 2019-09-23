from django.db.models import Prefetch
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from events.models import Event
from promoters.models import PromoterSpace
from tickets.filters import TicketFilterSet
from tickets.permissions import CanUseTicketPermission
from .models import Ticket
from .serializers import TicketSerializer, MyTicketsSerializer


class TicketViewSet(XLSXFileMixin, ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated, DRYPermissions, )
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, XLSXRenderer, )
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = TicketFilterSet
    ordering_fields = (
        'event__name',
        'event_start_datetime',
    )

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

    @action(methods=['post', ], detail=True, url_path="mark-used-ticket")
    def mark_used_ticket(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.already_used = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class MyTicketsView(APIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        tickets = Ticket.objects.filter(user=user).cache()
        return Response(MyTicketsSerializer({'user': user, 'tickets': tickets}, context={'request': request}).data)


class UserTicketViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated, DRYPermissions, CanUseTicketPermission)

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
