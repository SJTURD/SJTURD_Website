# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20160906_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userext',
            name='wechat',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
    ]
