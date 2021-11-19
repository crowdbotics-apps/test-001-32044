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
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="book_movie",
    )
