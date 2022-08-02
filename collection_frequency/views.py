from rest_framework import viewsets
from .models import *
from .serializers import *


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class BinViewSet(viewsets.ModelViewSet):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer


class BinOperationViewSet(viewsets.ModelViewSet):
    queryset = BinOperation.objects.all()
    serializer_class = BinOperationSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BinOperationListSerializer
        else:
            return BinOperationSerializer
