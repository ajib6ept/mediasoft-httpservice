from django.contrib import admin
from django.urls import path

from mediasoft.httpservice.views import CityViewSet, StreetViewSet

# router = routers.DefaultRouter()
# router.register(r"city/street", StreetViewSet)
# router.register(r"shop", ShopViewSet)
# "<int:city_iid>/street/",


urlpatterns = [
    # path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path(
        "<int:city_id>/street/",
        StreetViewSet.as_view({"get": "list"}),
        name="street-list",
    ),
    path("city/", CityViewSet.as_view({"get": "list"}), name="city-list"),
]
