from django.conf import settings
from django.db import models


class Car(models.Model):
    "Generated Model"
    brand = models.CharField(
        max_length=256,
    )
    color = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )


class Movie(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=100,
    )


class Book(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=256,
    )
    movie = models.ForeignKey(
        "home.Movie",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="book_movie",
    )


class Airplane(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    passenger_count = models.IntegerField(
        null=True,
        blank=True,
    )
