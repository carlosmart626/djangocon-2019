from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from .models import Promoter, PromoterSpace
from .serializers import PromoterSerializer, PromoterSpaceSerializer


class PromoterViewSet(ModelViewSet):
    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'name', 'is_active', 'contact_name', ]


class PromoterSpaceViewSet(ModelViewSet):
    queryset = PromoterSpace.objects.all()
    serializer_class = PromoterSpaceSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'name', 'promoter', 'capacity', 'description']
