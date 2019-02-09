# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-21 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=100)),
                ('password', models.IntegerField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('fathername', models.CharField(max_length=300)),
                ('mothername', models.CharField(max_length=300)),
                ('dob', models.CharField(max_length=300)),
                ('age', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=300)),
                ('maritalstatus', models.CharField(max_length=300)),
                ('mobilenumber', models.CharField(max_length=300)),
                ('emailid', models.CharField(max_length=300)),
                ('qualification', models.CharField(max_length=300)),
                ('income', models.CharField(max_length=300)),
                ('panno', models.CharField(max_length=300)),
                ('aadharnumber', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
            ],
        ),
    ]