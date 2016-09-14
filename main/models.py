# coding:utf-8
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)


class LFOffice(models.Model):
    name = models.CharField(max_length=128)
    detail = models.CharField(max_length=256, blank=True)
    contact = models.CharField(max_length=256, blank=True)


class Location(models.Model):
    name = models.CharField(max_length=128)


class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    USER_TYPE_CHOICES = (
        (0, 'superuser'),
        (1, 'staff'),
        (2, 'user'),
    )
    user_type = models.SmallIntegerField(choices=USER_TYPE_CHOICES)
    user_id = models.IntegerField()
    username = models.CharField(max_length=150)

    OPERATION_TYPE_CHOICES = (
        (0, 'ADD'),
        (1, 'EDIT'),
        (2, 'DELETE'),
        (3, 'PAIR'),
    )
    operation_type = models.SmallIntegerField(choices=OPERATION_TYPE_CHOICES)

    OBJECT_TYPE_CHOICES = (
        (0, 'User'),
        (1, 'Category'),
        (2, 'LFOffice'),
        (3, 'Location'),
        (4, 'Lost'),
        (5, 'Found'),
    )
    object_type = models.SmallIntegerField(choices=OBJECT_TYPE_CHOICES)
    object_id = models.IntegerField()

    detail = models.CharField(max_length=512)
