# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='closedate',
            new_name='closeddate',
        ),
    ]
