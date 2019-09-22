from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from .models import Event
from .serializers import EventSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'name', 'promoter', 'space', 'description']
