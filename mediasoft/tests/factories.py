from datetime import time
from random import randint

import factory
from faker import Factory

from mediasoft.httpservice.models import City, Shop, Street

factory.Faker._DEFAULT_LOCALE = "ru_RU"


faker = Factory.create()

MAX_NUMBER = 1
MIN_NUMBER = 1000

MIN_HOUR = 1
MAX_HOUR = 11


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = factory.Faker("city_name")


class StreetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Street

    name = factory.Faker("street_name")
    city = factory.SubFactory(CityFactory)


class ShopFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shop

    name = factory.Faker("company")
    city = factory.SubFactory(CityFactory)
    street = factory.SubFactory(StreetFactory)
    number = factory.LazyAttribute(
        lambda x: randint(MAX_NUMBER, MIN_NUMBER + 1)
    )
    opening_time = factory.LazyAttribute(
        lambda x: time(hour=randint(MIN_HOUR, MAX_HOUR))
    )

    closing_time = factory.LazyAttribute(
        lambda x: time(hour=randint(MAX_HOUR + 1, MAX_HOUR * 2))
    )
