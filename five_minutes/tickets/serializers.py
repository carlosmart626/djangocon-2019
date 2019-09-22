from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from events.models import Event
from events.serializers import EventSerializer
from users.models import User
from users.serializers import UserSerializer
from .models import Ticket


class TicketSerializer(ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(source='event', queryset=Event.objects.all())
    event = EventSerializer(read_only=True, fields=EventSerializer.get_nested_fields())
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    user = UserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = (
            'id',
            'event_id',
            'event',
            'user_id',
            'user',
            'already_used'
        )
