from .models import Vehicle, NavigationRecord
from .serializers import VehicleSerializer, NavigationRecordSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

CACHE_TTL = getattr(settings, 'CACHE_TLL', DEFAULT_TIMEOUT)


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super(VehicleViewSet, self).dispatch(*args, **kwargs)


class NavigationRecordViewSet(viewsets.ModelViewSet):
    queryset = NavigationRecord.objects.all()
    serializer_class = NavigationRecordSerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super(NavigationRecordViewSet, self).dispatch(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        last_48_hour = timezone.now() - timezone.timedelta(hours=48)
        queryset = NavigationRecord.objects.filter(datetime__gte=(last_48_hour.date(), timezone.now()))
        serializer = NavigationRecordSerializer(queryset, many=True)

        return Response(serializer.data, status=200)
