from rest_framework import serializers

from mediasoft.httpservice.models import City, Shop, Street


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ["name"]


class ShopSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data["opening_time"] >= data["closing_time"]:
            raise serializers.ValidationError(
                "closing time must be more than the opening time"
            )

        if data["street"].city.id != data["city"].id:
            raise serializers.ValidationError("incorrect street id")
        return data

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
