from django.utils import timezone
from django.db import models
import uuid


class TeddyStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hunger = models.PositiveIntegerField(default=0)
    thirst = models.PositiveIntegerField(default=0)
    last_fed_time = models.DateTimeField(default=timezone.now)
    last_drink_time = models.DateTimeField(default=timezone.now)
    cleanliness = models.PositiveIntegerField(default=100)
    last_clean_time = models.DateTimeField(default=timezone.now)
    happiness = models.PositiveIntegerField(default=100)
    last_happy_time = models.DateTimeField(default=timezone.now)
    excited = models.PositiveIntegerField(default=50)
    last_play_time = models.DateTimeField(default=timezone.now)
    sleepiness = models.PositiveIntegerField(default=0)
    last_sleep_time = models.DateTimeField(default=timezone.now)
    last_awake_time = models.DateTimeField(default=timezone.now)
    desier = models.CharField(max_length=32, blank=True)
    sentense = models.CharField(max_length=128, blank=True)
