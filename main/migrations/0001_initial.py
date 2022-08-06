# Generated by Django 4.0.6 on 2022-07-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Equipment',
                'verbose_name_plural': 'Equipments',
            },
        ),
    ]