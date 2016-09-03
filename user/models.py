from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class UserExt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=128, unique=True, blank=False)

    GENDER_CHOICES = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
        (3, '其他'),
    )

    TYPE_CHOICES = (
        (0, '未知'),
        (1, '本科生'),
        (2, '研究生'),
        (3, '博士生'),
        (4, '教职工'),
    )

    jaccount = models.CharField(max_length=256, unique=True, blank=True)
    name = models.CharField(max_length=128, blank=True)
    gender = models.SmallIntegerField(blank=True, choices=GENDER_CHOICES)
    email = models.CharField(max_length=128, unique=True, blank=True)
    phone = models.CharField(max_length=32, unique=True, blank=True,
                             validators=[RegexValidator(regex=r'1\d{10}',
                                                        message='手机号码不合法', code='Invalid phone number')])
    type = models.SmallIntegerField(blank=True, choices=TYPE_CHOICES)

    score = models.IntegerField(default=0, blank=False)
    money = models.IntegerField(default=0, blank=False)

    wechat = models.CharField(max_length=256, unique=True, blank=True)
