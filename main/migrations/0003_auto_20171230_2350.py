# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-30 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171230_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actphoto',
            name='photo',
            field=models.ImageField(upload_to='actphoto', verbose_name='활동 사진'),
        ),
    ]
