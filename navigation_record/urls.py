from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import VehicleViewSet, NavigationRecordViewSet

router = DefaultRouter()

router.register('vehicle', VehicleViewSet)
router.register('navigation', NavigationRecordViewSet)

app_name = 'navigation_record'

urlpatterns = [
    path('', include(router.urls)),
]
