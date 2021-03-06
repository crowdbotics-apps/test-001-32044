# Generated by Django 2.2.24 on 2021-11-19 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20211119_1640"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="movie",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="book_movie",
                to="home.Movie",
            ),
        ),
    ]
