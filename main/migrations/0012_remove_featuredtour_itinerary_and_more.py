# Generated by Django 4.0.6 on 2022-10-06 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_ytvideo_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuredtour',
            name='itinerary',
        ),
        migrations.DeleteModel(
            name='FeaturedCartegory',
        ),
        migrations.DeleteModel(
            name='FeaturedTour',
        ),
    ]