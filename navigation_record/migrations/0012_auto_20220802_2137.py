# Generated by Django 3.0.1 on 2022-08-02 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation_record', '0011_auto_20220802_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationrecord',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 21, 37, 47, 408394)),
        ),
    ]
