# Generated by Django 3.0.6 on 2020-05-31 14:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0004_auto_20200531_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 14, 19, 14, 593720, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 14, 19, 14, 592720, tzinfo=utc)),
        ),
    ]