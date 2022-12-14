from datetime import datetime

from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey("City", models.CASCADE)
    street = models.ForeignKey("Street", models.CASCADE)
    number = models.CharField(max_length=5)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]

    @property
    def is_open(self):
        return (
            "1"
            if self.opening_time <= datetime.now().time() < self.closing_time
            else "0"
        )


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey("City", models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.city.name}"

    class Meta:
        ordering = ["-id"]
