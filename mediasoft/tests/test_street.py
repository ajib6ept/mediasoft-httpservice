from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from mediasoft.httpservice.models import Street
from mediasoft.tests.factories import StreetFactory


class CityTests(APITestCase):
    def setUp(self):
        self.test_url = reverse("street-list", kwargs={"city_id": 1})

    def test_view_cities(self):
        StreetFactory.create_batch(50)
        response = self.client.get(self.test_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        streets = list(Street.objects.filter(city_id=1).values("name"))
        results = response.data.get("results")
        self.assertEqual(streets, results)

    def test_view_cities_with_other_methods(self):
        response = self.client.post(self.test_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put(self.test_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.delete(self.test_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_url(self):
        test_url = reverse("street-list", kwargs={"city_id": "0"})
        response = self.client.put(test_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
