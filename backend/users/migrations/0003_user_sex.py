# Generated by Django 2.2.24 on 2021-11-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20211119_1602"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="sex",
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
