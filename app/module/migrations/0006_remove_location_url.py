# Generated by Django 4.2.4 on 2023-08-26 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0005_location_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='url',
        ),
    ]