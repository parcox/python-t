# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-28 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20170428_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.TextField(blank=True, max_length=128, verbose_name='адрес доставки по-умолчанию'),
        ),
    ]
