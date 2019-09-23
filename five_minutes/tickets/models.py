import uuid
from django.db import models

from events.models import Event
from users.models import User


class Ticket(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False, db_index=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tickets')
    already_used = models.BooleanField(default=False)

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        # return True
        return request.user == self.user

    @staticmethod
    def has_write_permission(request):
        return False

    @staticmethod
    def has_create_permission(request):
        return True
