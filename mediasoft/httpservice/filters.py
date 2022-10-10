import django_filters

from mediasoft.httpservice.models import Shop

STATUS_CHOICES = (
    (0, "False"),
    (1, "True"),
)


class ShopFilter(django_filters.FilterSet):

    city = django_filters.NumberFilter(field_name="city_id")
    street = django_filters.NumberFilter(field_name="street_id")
    open = django_filters.ChoiceFilter(
        choices=STATUS_CHOICES, method="ids__in"
    )

    def ids__in(self, queryset, value, *args, **kwargs):
        shop_status = args[0]
        shops_ids = [
            shop.id for shop in queryset if shop.is_open == shop_status
        ]
        queryset = queryset.filter(id__in=shops_ids)
        return queryset

    class Meta:
        model = Shop
        fields = ["city_id", "street_id"]
