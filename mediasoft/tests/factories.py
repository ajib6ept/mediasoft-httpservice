import factory
from faker import Factory

from mediasoft.httpservice.models import City, Street

factory.Faker._DEFAULT_LOCALE = "ru_RU"


faker = Factory.create()


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = factory.Faker("city_name")


class StreetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Street

    name = factory.Faker("street_name")
    city = factory.SubFactory(CityFactory)
