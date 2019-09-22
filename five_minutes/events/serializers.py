from rest_framework import serializers

from five_minutes.serializers import DynamicModelSerializer
from promoters.models import Promoter, PromoterSpace
from promoters.serializers import PromoterSerializer, PromoterSpaceSerializer
from .models import Event


class EventSerializer(DynamicModelSerializer):
    promoter_id = serializers.PrimaryKeyRelatedField(source='promoter', queryset=Promoter.objects.all())
    promoter = PromoterSerializer(read_only=True)
    space_id = serializers.PrimaryKeyRelatedField(source='space', queryset=PromoterSpace.objects.all())
    space = PromoterSpaceSerializer(read_only=True, fields=PromoterSpaceSerializer.get_location_fields())

    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'start_datetime',
            'end_datetime',
            'promoter_id',
            'promoter',
            'space_id',
            'space',
            'description'
        )

    @staticmethod
    def get_nested_fields():
        return 'id', 'name', 'start_datetime', 'end_datetime', 'space'
