# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-01 07:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0056_auto_20170601_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variantfilter',
            name='unit',
        ),
    ]
