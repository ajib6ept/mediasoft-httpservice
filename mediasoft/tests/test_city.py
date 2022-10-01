from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from mediasoft.tests.factories import CityFactory


class CityTests(APITestCase):
    def test_view_cities(self):
        cities = CityFactory.create_batch(5)
        response = self.client.get(reverse("city-list"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get("results")
        results_list = [result["name"] for result in results]
        for city in cities:
            self.assertIn(city.name, results_list)

    def test_view_cities_with_other_methods(self):
        response = self.client.post(reverse("city-list"), format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put(reverse("city-list"), format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.delete(reverse("city-list"), format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
