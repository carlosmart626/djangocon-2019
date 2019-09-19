from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from .models import Promoter, PromoterSpace
from .serializers import PromoterSerializer, PromoterSpaceSerializer


class PromoterViewSet(ModelViewSet):
    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer
    permission_classes = [IsAuthenticated, ]


class PromoterSpaceViewSet(ModelViewSet):
    queryset = PromoterSpace.objects.all()
    serializer_class = PromoterSpaceSerializer
    permission_classes = [IsAuthenticated, ]
