# Generated by Django 4.2.8 on 2023-12-12 19:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attractions", "0006_attraction_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attraction",
            name="rating",
            field=models.IntegerField(
                default=3,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
    ]
