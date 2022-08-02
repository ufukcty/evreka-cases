from django.db import models
from datetime import datetime


class Vehicle(models.Model):
    objects = None
    plate = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.plate}"

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


class NavigationRecord(models.Model):
    objects = None
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.now())
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return f"{self.vehicle}"

    class Meta:
        verbose_name = 'Navigation Record'
        verbose_name_plural = 'Navigation Records'
