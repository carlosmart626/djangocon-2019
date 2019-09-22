from rest_framework import serializers

from five_minutes.serializers import DynamicModelSerializer
from .models import Promoter, PromoterSpace


class PromoterSerializer(DynamicModelSerializer):

    class Meta:
        model = Promoter
        fields = '__all__'

    @staticmethod
    def get_nested_fields():
        return 'id', 'name'


class PromoterSpaceSerializer(DynamicModelSerializer):
    promoter_id = serializers.PrimaryKeyRelatedField(source='promoter', queryset=Promoter.objects.all())
    promoter = PromoterSerializer(read_only=True, fields=PromoterSerializer.get_nested_fields())

    class Meta:
        model = PromoterSpace
        fields = (
            'id',
            'name',
            'promoter_id',
            'promoter',
            'capacity',
            'description',
        )

    @staticmethod
    def get_location_fields():
        return 'name', 'description'
