# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter', '0003_auto_20161113_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
