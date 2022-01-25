from django.db import models
import uuid


class LittleSealStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hunger = models.PositiveIntegerField(default=0)
    thirst = models.PositiveIntegerField(default=0)
    cleanliness = models.PositiveIntegerField(default=100)
    happiness = models.PositiveIntegerField(default=100)
    excited = models.PositiveIntegerField(default=50)
    sleepiness = models.PositiveIntegerField(default=0)
    desier = models.CharField(max_length=32)
    sentense = models.CharField(max_length=128)
