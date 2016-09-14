# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='phone',
            field=models.CharField(blank=True, max_length=32, validators=[django.core.validators.RegexValidator(regex=b'1\\d{10}', message=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81\xe4\xb8\x8d\xe5\x90\x88\xe6\xb3\x95', code=b'Invalid phone number')]),
        ),
        migrations.AlterField(
            model_name='lost',
            name='thank',
            field=models.SmallIntegerField(choices=[(0, b'\xe6\x9c\xaa\xe9\x80\x89\xe6\x8b\xa9\xe7\xad\x94\xe8\xb0\xa2'), (1, b'\xe7\xad\x94\xe8\xb0\xa2')]),
        ),
    ]
