import json
import urllib.parse
from datetime import datetime, timedelta
from pathlib import Path

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from mediasoft.tests.factories import ShopFactory, StreetFactory, build_shop

FIXTURE_DIR = Path(__file__).resolve().parent.joinpath("fixtures")
BAD_SHOP_FIXTURE_FILES = (
    "bad_shop_json1.json",
    "bad_shop_json2.json",
    "bad_shop_json3.json",
    "bad_shop_json4.json",
    "bad_shop_json5.json",
)

BAD_SHOP_FILTERS = (
    {"street": "1", "city": "1", "open": "2"},
    {"street": "1", "city": "1", "open": "A"},
    {"street": "1", "city": "A", "open": "1"},
    {"street": "A", "city": "1", "open": "0"},
)

OPEN_SHOP_PARAMETRS = {
    "opening_time": datetime.now().time(),
    "closing_time": (datetime.now() + timedelta(hours=1)).time(),
    "city_id": 1,
    "street_id": 1,
}

CLOSE_SHOP_PARAMERS = {
    "opening_time": (datetime.now() - timedelta(hours=1)).time(),
    "closing_time": datetime.now().time(),
    "city_id": 1,
    "street_id": 2,
}

SHOP_FILTERS_COUNT = (
    ({"street": "1", "city": "1"}, 1),
    ({"city": "1"}, 2),
    ({"street": "2"}, 1),
    ({"open": "1"}, 1),
    ({"open": "0"}, 1),
    ({"street": "2", "city": "1", "open": "1"}, 0),
    ({"street": "1", "city": "1", "open": "1"}, 1),
)


class ShopCreateTests(APITestCase):
    def test_create_shop(self):
        shop_json = build_shop()
        response = self.client.post(
            reverse("shop"),
            shop_json,
            format="json",
        )
        results = response.data["data"]["results"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(results, 1)

    def test_view_cities_with_other_methods(self):

        response = self.client.put(reverse("shop"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.delete(reverse("shop"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_shop_with_bad_paramers(self):

        # is needed to check if the json contains a street from another city
        StreetFactory.create_batch(3)

        for bad_shop_file in BAD_SHOP_FIXTURE_FILES:
            bad_shop_path = Path(FIXTURE_DIR).joinpath(bad_shop_file)
            bad_shop_json = json.loads(Path(bad_shop_path).read_text())
            response = self.client.post(
                reverse("shop"),
                bad_shop_json,
                format="json",
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ShopViewTests(APITestCase):
    def create_shop_filter_url(self, shop_filter):
        return urllib.parse.urljoin(
            reverse("shop"), "?" + urllib.parse.urlencode(shop_filter)
        )

    def test_bad_shop_filters(self):
        for shop_filter in BAD_SHOP_FILTERS:
            shop_filter_url = self.create_shop_filter_url(shop_filter)
            response = self.client.get(shop_filter_url)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_shop_filters(self):

        ShopFactory.create(**OPEN_SHOP_PARAMETRS)
        ShopFactory.create(**CLOSE_SHOP_PARAMERS)

        for shop_filter, shop_count in SHOP_FILTERS_COUNT:
            shop_filter_url = self.create_shop_filter_url(shop_filter)
            response = self.client.get(shop_filter_url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(shop_count, response.data["count"])
