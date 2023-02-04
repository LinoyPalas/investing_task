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


class CreativeViewSet(viewsets.ModelViewSet):
    # set to the relevant model instances
    queryset = Creative.objects.all()

    # set to the relevant serializer class
    serializer_class = CreativeSerializer


class LineItemsByTargetingView(viewsets.ModelViewSet):
    # set to the relevant model instances
    queryset = LineItem.objects.all()

    # set to the relevant serializer class
    serializer_class = LineItemSerializer

    def get_queryset(self):
        """allows filtering by the targeting parameters"""

        country = self.request.query_params.get('country', None)
        language = self.request.query_params.get('language', None)
        device = self.request.query_params.get('device', None)
        os = self.request.query_params.get('os', None)
        browser = self.request.query_params.get('browser', None)

        queryset = self.queryset.filter(ad_unit__country__contains=country,
                                        ad_unit__language__contains=language,
                                        ad_unit__device__contains=device,
                                        ad_unit__os__contains=os,
                                        ad_unit__browser__contains=browser)
        return queryset
