# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-08-31 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]