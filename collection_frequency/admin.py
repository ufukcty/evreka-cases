from django.contrib import admin
from .models import Bin, Operation, BinOperation


@admin.register(Operation)
class Operation(admin.ModelAdmin):
    list_filter = ("name",)
    list_display = ("name",)


@admin.register(Bin)
class Bin(admin.ModelAdmin):
    list_filter = ("latitude", "longitude",)
    list_display = ("latitude", "longitude",)


@admin.register(BinOperation)
class BinOperation(admin.ModelAdmin):
    list_filter = ("operation", "collection_frequency", "last_collection",)
    list_display = ("operation", "collection_frequency", "last_collection",)
