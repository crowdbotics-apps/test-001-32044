from django.contrib import admin
from .models import Book, Car, Movie

admin.site.register(Car)
admin.site.register(Movie)
admin.site.register(Book)

# Register your models here.
