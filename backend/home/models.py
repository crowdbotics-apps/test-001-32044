from django.conf import settings
from django.db import models


class Car(models.Model):
    "Generated Model"
    brand = models.CharField(
        max_length=256,
    )
