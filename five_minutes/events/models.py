from django.db import models

from promoters.models import Promoter, PromoterSpace


class Event(models.Model):
    name = models.CharField(max_length=140)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    promoter = models.ForeignKey(Promoter, on_delete=models.CASCADE, related_name='promoter_events')
    space = models.ForeignKey(PromoterSpace, on_delete=models.CASCADE, related_name='space_events')
    description = models.TextField(default="")
