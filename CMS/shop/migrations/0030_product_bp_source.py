# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-17 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20170513_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bp_source',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]