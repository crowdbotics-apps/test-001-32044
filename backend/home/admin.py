from django.contrib import admin
from .models import Airplane, Book, Car, Movie

admin.site.register(Car)
admin.site.register(Movie)
admin.site.register(Book)
admin.site.register(Airplane)

# Register your models here.
