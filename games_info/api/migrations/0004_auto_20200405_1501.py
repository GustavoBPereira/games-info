# Generated by Django 3.0.4 on 2020-04-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200405_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='time_information',
            field=models.ManyToManyField(related_name='time_information', to='api.TimeData'),
        ),
    ]
