# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_lostitem_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lostitem',
            old_name='STATUS',
            new_name='status',
        ),
    ]
