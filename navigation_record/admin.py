from django.contrib import admin
from .models import Vehicle, NavigationRecord


@admin.register(Vehicle)
class Vehicle(admin.ModelAdmin):
    list_filter = ("plate",)
    list_display = ("plate",)


@admin.register(NavigationRecord)
class NavigationRecord(admin.ModelAdmin):
    list_filter = ("vehicle", "datetime", "latitude", "longitude")
    list_display = ("vehicle", "datetime", "latitude", "longitude")
