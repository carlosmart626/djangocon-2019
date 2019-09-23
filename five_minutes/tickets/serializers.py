from dry_rest_permissions.generics import DRYPermissionsField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

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
    permissions = DRYPermissionsField()

    class Meta:
        model = Ticket
        fields = (
            'id',
            'event_id',
            'event',
            'user_id',
            'user',
            'already_used',
            'permissions',
        )


class MyTicketsSerializer(Serializer):
    user = UserSerializer(read_only=True)
    tickets = TicketSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
