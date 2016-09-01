# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='found',
            name='category',
        ),
        migrations.RemoveField(
            model_name='found',
            name='lfoffice',
        ),
        migrations.RemoveField(
            model_name='found',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='lost',
            name='location',
        ),
        migrations.RemoveField(
            model_name='lost',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userext',
            name='user',
        ),
        migrations.DeleteModel(
            name='Found',
        ),
        migrations.DeleteModel(
            name='Lost',
        ),
        migrations.DeleteModel(
            name='UserExt',
        ),
    ]
