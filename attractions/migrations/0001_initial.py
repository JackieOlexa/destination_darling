# Generated by Django 4.2.8 on 2023-12-08 03:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("destinations", "0005_delete_attraction"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Attraction",
            fields=[
                ("name", models.TextField(primary_key=True, serialize=False)),
                ("description", models.TextField()),
                ("address", models.TextField()),
                (
                    "rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("tags", models.TextField()),
                ("numberReviews", models.IntegerField(default=1)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="destinations.destination",
                    ),
                ),
            ],
        ),
    ]