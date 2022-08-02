from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register('operation', OperationViewSet)
router.register('bin', BinViewSet)
router.register('bin-operation', BinOperationViewSet)

app_name = 'collection_frequency'


urlpatterns = [
    path("", include(router.urls))
]