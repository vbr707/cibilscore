# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-28 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankadmin', '0007_auto_20180627_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankreport',
            name='mobilenumber',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankreport',
            name='name',
            field=models.CharField(default='exit', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankreport',
            name='pancard',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
