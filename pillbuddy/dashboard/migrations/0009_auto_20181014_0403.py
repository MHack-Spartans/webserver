# Generated by Django 2.1.2 on 2018-10-14 04:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20181014_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='next_dispense',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 14, 4, 3, 45, 160291)),
        ),
    ]
