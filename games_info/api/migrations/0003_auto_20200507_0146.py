# Generated by Django 3.0.4 on 2020-05-07 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200503_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='time_information',
        ),
        migrations.AddField(
            model_name='game',
            name='time_information',
            field=models.ManyToManyField(related_name='time_information', to='api.TimeData'),
        ),
    ]