from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Promoter, PromoterSpace


class PromoterSerializer(ModelSerializer):

    class Meta:
        model = Promoter
        fields = '__all__'


class PromoterSpaceSerializer(ModelSerializer):
    promoter_id = serializers.PrimaryKeyRelatedField(source='promoter', queryset=Promoter.objects.all())
    promoter = PromoterSerializer(read_only=True)

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
