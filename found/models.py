from django.core.validators import RegexValidator
from django.db import models


class Found(models.Model):
    user = models.ForeignKey('user.UserExt', on_delete=models.CASCADE, default=1)
    category = models.ForeignKey('main.Category', on_delete=models.SET_DEFAULT, default=1)
    lfoffice = models.ForeignKey('main.LFOffice', on_delete=models.SET_DEFAULT, default=1)
    picture = models.ImageField(upload_to='found', null=True, blank=True, default=None)
    detail = models.CharField(max_length=256, blank=True)

    phone = models.CharField(max_length=32, blank=True,
                             validators=[RegexValidator(regex=r'1\d{10}',
                                                        message='手机号码不合法', code='Invalid phone number')])
    email = models.EmailField(max_length=128, blank=True)
    remark = models.CharField(max_length=256, blank=True)

    date = models.DateTimeField(auto_now_add=True)

    paired = models.BooleanField(default=False)
