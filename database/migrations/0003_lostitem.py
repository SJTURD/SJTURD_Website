# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20160927_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='LostItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('lost_time', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
            ],
        ),
    ]
