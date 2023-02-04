from rest_framework import viewsets
from .models import AdUnit, LineItem, Creative
from .serializers import AdUnitSerializer, LineItemSerializer, CreativeSerializer


class AdUnitViewSet(viewsets.ModelViewSet):
    # set to the relevant model instances
    queryset = AdUnit.objects.all()

    # set to the relevant serializer class
    serializer_class = AdUnitSerializer


