# Generated by Django 5.0.6 on 2024-05-22 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rajesh_cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='make',
        ),
        migrations.RemoveField(
            model_name='car',
            name='vin',
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]