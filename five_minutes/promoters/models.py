from django.db import models


class Promoter(models.Model):
    name = models.CharField(max_length=140)
    is_active = models.BooleanField(default=True)
    contact_name = models.CharField(max_length=140)
    contact_phone = models.CharField(max_length=32)
    website = models.URLField(max_length=140)


class PromoterSpace(models.Model):
    name = models.CharField(max_length=140)
    promoter = models.ForeignKey(Promoter, on_delete=models.CASCADE, related_name='spaces')
    capacity = models.PositiveIntegerField(default=0)
    description = models.TextField()
