# Generated by Django 4.0.6 on 2022-10-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0009_itinerary_departure_date_itinerary_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='is_upcoming',
            field=models.BooleanField(default=False),
        ),
    ]
