# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter', '0007_auto_20161114_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, upload_to='profile_pic/'),
        ),
    ]
