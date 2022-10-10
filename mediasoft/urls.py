from django.contrib import admin
from django.urls import path

from mediasoft.httpservice.views import CityViewSet, ShopViewSet, StreetViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "<int:city_id>/street/",
        StreetViewSet.as_view({"get": "list"}),
        name="street-list",
    ),
    path("city/", CityViewSet.as_view({"get": "list"}), name="city-list"),
    path("shop/", ShopViewSet.as_view(), name="shop"),
]
