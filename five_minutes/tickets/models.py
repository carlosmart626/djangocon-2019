import uuid
from django.db import models

from events.models import Event
from users.models import User


class Ticket(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False, db_index=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tickets')
    already_used = models.BooleanField(default=False)
