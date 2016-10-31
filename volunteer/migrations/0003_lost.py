# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('volunteer', '0002_delete_lost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('lost_time', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=0)),
                ('img', models.FileField(upload_to='./lost/')),
            ],
        ),
    ]
