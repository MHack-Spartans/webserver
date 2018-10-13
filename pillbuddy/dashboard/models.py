from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=30)
    short_desc = models.CharField(max_length=30)
    per_day = models.IntegerField()
    pillsTaken = models.IntegerField()
    objects = models.Manager()


class Schedule(models.Model):
    drug = models.CharField(max_length=30)
    frequency = models.CharField(max_length=30)
    first_dispense = models.DateField