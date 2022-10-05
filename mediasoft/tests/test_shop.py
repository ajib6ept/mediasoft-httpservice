import json
from pathlib import Path

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from mediasoft.tests.factories import ShopFactory, StreetFactory

FIXTURE_DIR = Path(__file__).resolve().parent.joinpath("fixtures")
BAD_FIXTURE_FILES = (
    "bad_shop_json1.json",
    "bad_shop_json2.json",
    "bad_shop_json3.json",
    "bad_shop_json4.json",
    "bad_shop_json5.json",
)


class ShopTests(APITestCase):
    def build_shop(self):
        new_street = StreetFactory.create()
        new_shop = ShopFactory.build()
        return {
            "name": new_shop.name,
            "city": new_street.city.id,
            "street": new_street.id,
            "number": new_shop.number,
            "opening_time": str(new_shop.opening_time),
            "closing_time": str(new_shop.closing_time),
        }

    def test_create_shop(self):
        shop_json = self.build_shop()
        response = self.client.post(
            reverse("shop-create"),
            shop_json,
            format="json",
        )
        results = response.data["data"]["results"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(results, 1)

    def test_view_cities_with_other_methods(self):
        shop_json = self.build_shop()

        response = self.client.get(reverse("shop-create"), format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put(
            reverse("shop-create"), shop_json, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.delete(
            reverse("shop-create"), shop_json, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_shop_with_bad_paramers(self):

        # is needed to check if the json contains a street from another city
        StreetFactory.create_batch(3)

        for bad_shop_file in BAD_FIXTURE_FILES:
            bad_shop_path = Path(FIXTURE_DIR).joinpath(bad_shop_file)
            bad_shop_json = json.loads(Path(bad_shop_path).read_text())
            response = self.client.post(
                reverse("shop-create"),
                bad_shop_json,
                format="json",
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
