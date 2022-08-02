from .models import Vehicle, NavigationRecord
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['plate']


class NavigationRecordSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source='vehicle.plate', read_only=True)

    class Meta:
        model = NavigationRecord
        fields = ['vehicle_plate', 'datetime', 'latitude', 'longitude']
