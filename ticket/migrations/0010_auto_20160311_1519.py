# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0009_auto_20160311_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='number',
            field=models.FloatField(default=1),
        ),
    ]
