from rest_framework import viewsets
from investing_task.models import AdUnit, LineItem, Creative
from investing_task.serializers import AdUnitSerializer, LineItemSerializer, CreativeSerializer


class AdUnitViewSet(viewsets.ModelViewSet):
    # set to the relevant model instances
    queryset = AdUnit.objects.all()

    # set to the relevant serializer class
    serializer_class = AdUnitSerializer


class LineItemViewSet(viewsets.ModelViewSet):
    # set to the relevant model instances
    queryset = LineItem.objects.all()

    # set to the relevant serializer class
    serializer_class = LineItemSerializer

    def get_queryset(self):
        """allows filtering by the targeting parameters"""

        queryset = self.queryset
        country = self.request.query_params.get('country', None)
        language = self.request.query_params.get('language', None)
        device = self.request.query_params.get('device', None)
        os = self.request.query_params.get('os', None)
        browser = self.request.query_params.get('browser', None)

        if country is not None:
            queryset = queryset.filter(ad_unit__country=country)
        if language is not None:
            queryset = queryset.filter(ad_unit__language=language)
        if device is not None:
            queryset = queryset.filter(ad_unit__device=device)
        if os is not None:
            queryset = queryset.filter(ad_unit__os=os)
        if browser is not None:
            queryset = queryset.filter(ad_unit__browser=browser)
        return queryset


class CreativeViewSet(viewsets.ModelViewSet):
    # set to the relevant model instances
    queryset = Creative.objects.all()

    # set to the relevant serializer class
    serializer_class = CreativeSerializer
