# Generated by Django 4.0.2 on 2022-02-01 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 2, 1, 16, 14, 20, 833935)),
        ),
    ]