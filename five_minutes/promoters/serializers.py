from rest_framework.serializers import ModelSerializer

from .models import Promoter, PromoterSpace


class PromoterSerializer(ModelSerializer):

    class Meta:
        model = Promoter
        fields = '__all__'


class PromoterSpaceSerializer(ModelSerializer):

    class Meta:
        model = PromoterSpace
        fields = '__all__'
