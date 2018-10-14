from django.db import models
from datetime import datetime

class Drug(models.Model):
    name = models.CharField(max_length=30)
    short_desc = models.CharField(max_length=30)
    per_day = models.IntegerField()
    pillsTaken = models.IntegerField()
    slot = models.IntegerField() 
    objects = models.Manager()


class Schedule(models.Model):
    drug = models.CharField(max_length = 30, default = 'advil')
    frequency = models.CharField(max_length=30)
    next_dispense = models.DateTimeField(default = datetime.now())
    amount = models.IntegerField(default=1)
    objects = models.Manager()
