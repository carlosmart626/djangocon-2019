from rest_framework.serializers import ModelSerializer

from .models import Ticket


class TicketSerializer(ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'
