# Generated by Django 2.2.6 on 2019-10-11 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191011_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Post date'),
        ),
    ]