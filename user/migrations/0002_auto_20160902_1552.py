# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userext',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(0, b'\xe6\x9c\xaa\xe7\x9f\xa5'), (1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3'), (3, b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
        migrations.AlterField(
            model_name='userext',
            name='phone',
            field=models.CharField(blank=True, unique=True, max_length=32, validators=[django.core.validators.RegexValidator(regex=b'1\\d{10}', message=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81\xe4\xb8\x8d\xe5\x90\x88\xe6\xb3\x95', code=b'Invalid phone number')]),
        ),
        migrations.AlterField(
            model_name='userext',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(0, b'\xe6\x9c\xaa\xe7\x9f\xa5'), (1, b'\xe6\x9c\xac\xe7\xa7\x91\xe7\x94\x9f'), (2, b'\xe7\xa0\x94\xe7\xa9\xb6\xe7\x94\x9f'), (3, b'\xe5\x8d\x9a\xe5\xa3\xab\xe7\x94\x9f'), (4, b'\xe6\x95\x99\xe8\x81\x8c\xe5\xb7\xa5')]),
        ),
    ]
