# Generated by Django 4.0.1 on 2022-01-25 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teddybot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teddystatus',
            name='last_clean_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 2, 28, 15, 543891)),
        ),
        migrations.AddField(
            model_name='teddystatus',
            name='last_drink_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 2, 28, 15, 543857)),
        ),
        migrations.AddField(
            model_name='teddystatus',
            name='last_fed_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 2, 28, 15, 543817)),
        ),
        migrations.AddField(
            model_name='teddystatus',
            name='last_happy_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 2, 28, 15, 543921)),
        ),
        migrations.AddField(
            model_name='teddystatus',
            name='last_play_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 2, 28, 15, 543950)),
        ),
        migrations.AddField(
            model_name='teddystatus',
            name='last_sleep_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 2, 28, 15, 543982)),
        ),
        migrations.AlterField(
            model_name='teddystatus',
            name='desier',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='teddystatus',
            name='sentense',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
