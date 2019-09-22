from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from promoters.models import Promoter, PromoterSpace
from promoters.serializers import PromoterSerializer, PromoterSpaceSerializer
from .models import Event


class EventSerializer(ModelSerializer):
    promoter_id = serializers.PrimaryKeyRelatedField(source='promoter', queryset=Promoter.objects.all())
    promoter = PromoterSerializer(read_only=True)
    space_id = serializers.PrimaryKeyRelatedField(source='space', queryset=PromoterSpace.objects.all())
    space = PromoterSpaceSerializer(read_only=True)

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


class NestedEventSerializer(ModelSerializer):
    promoter_id = serializers.PrimaryKeyRelatedField(source='promoter', queryset=Promoter.objects.all())
    promoter = PromoterSerializer(read_only=True)
    space_id = serializers.PrimaryKeyRelatedField(source='space', queryset=PromoterSpace.objects.all())
    space = PromoterSpaceSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'start_datetime',
            'end_datetime',
            'promoter_id',
            'space_id',
            'description'
        )
