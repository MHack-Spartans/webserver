# Generated by Django 2.1.2 on 2018-10-14 04:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20181014_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='next_dispense',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 14, 4, 37, 1, 966565)),
        ),
    ]
