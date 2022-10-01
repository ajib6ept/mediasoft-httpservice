from rest_framework import serializers

from mediasoft.httpservice.models import City, Shop, Street


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ["name"]


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = [
            "name",
            "city",
            "street",
            "number",
            "opening_time",
            "closing_time",
        ]


class StreetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Street
        fields = ["name"]
