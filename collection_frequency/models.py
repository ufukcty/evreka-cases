from django.db import models


class Bin(models.Model):
    objects = None
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return f"{self.latitude}"


class Operation(models.Model):
    objects = None
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class BinOperation(models.Model):
    objects = None
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name='bin', related_query_name='bin', null=True)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name='operation', related_query_name='operation', null=True)
    collection_frequency = models.IntegerField(default=0)
    last_collection = models.DateTimeField()

    def __str__(self):
        return str(self.collection_frequency)
