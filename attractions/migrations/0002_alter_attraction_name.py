# Generated by Django 4.2.8 on 2023-12-08 03:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attractions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attraction",
            name="name",
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
