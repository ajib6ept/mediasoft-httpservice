from rest_framework import viewsets

from mediasoft.httpservice.models import City, Shop, Street
from mediasoft.httpservice.serializers import (CitySerializer, ShopSerializer,
                                               StreetSerializer)


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(city_id=self.kwargs.get("city_id"))


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    http_method_names = ["get"]
