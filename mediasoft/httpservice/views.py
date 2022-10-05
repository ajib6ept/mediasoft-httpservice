from rest_framework import generics, viewsets
from rest_framework.response import Response

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


class ShopViewSet(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_shop = serializer.save()

        return Response(
            {
                "status": 200,
                "message": "The store has been successfully saved",
                "data": {"results": new_shop.id},
            }
        )
