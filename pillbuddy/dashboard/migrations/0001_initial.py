# Generated by Django 2.1.2 on 2018-10-13 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_desc', models.CharField(max_length=30)),
                ('per_day', models.IntegerField()),
                ('pillsTaken', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.CharField(max_length=30)),
                ('frequency', models.CharField(max_length=30)),
            ],
        ),
    ]
