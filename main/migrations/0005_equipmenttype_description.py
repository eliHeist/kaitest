# Generated by Django 4.0.6 on 2022-07-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_equipment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmenttype',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]