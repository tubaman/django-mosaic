# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-26 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosaico', '0008_auto_20160220_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='html',
            field=models.TextField(verbose_name='HTML'),
        ),
    ]
