# Generated by Django 2.2.17 on 2021-03-10 21:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('team_10e_app', '0007_auto_20210310_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 21, 13, 36, 515939, tzinfo=utc)),
        ),
    ]
