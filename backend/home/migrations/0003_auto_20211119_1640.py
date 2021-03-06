# Generated by Django 2.2.24 on 2021-11-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_car"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="car",
            name="color",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
