# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-10-03 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Student1',
        ),
        migrations.RenameModel(
            old_name='Teacher',
            new_name='Teacher1',
        ),
    ]
