# coding:utf-8
import os
import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from SJTURD_Website import settings
from main.tasks import pic_compress


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join('found', filename)


class Found(models.Model):
    user = models.ForeignKey('user.UserExt', on_delete=models.CASCADE, default=1)
    category = models.ForeignKey('main.Category', on_delete=models.SET_DEFAULT, default=1)
    location = models.ForeignKey('main.Location', on_delete=models.SET_DEFAULT, default=1)
    lfoffice = models.ForeignKey('main.LFOffice', on_delete=models.SET_DEFAULT, default=1)
    picture = models.ImageField(upload_to=get_file_path, null=True, blank=True, default=None)
    detail = models.CharField(max_length=256, blank=True)

    phone = models.CharField(max_length=32, blank=True,
                             validators=[RegexValidator(regex=r'1\d{10}',
                                                        message='手机号码不合法', code='Invalid phone number')])
    email = models.EmailField(max_length=128, blank=True)
    remark = models.CharField(max_length=256, blank=True)

    date = models.DateTimeField(auto_now_add=True)

    paired = models.BooleanField(default=False)


@receiver(post_save, sender=Found)
def create_thumbnail(sender, instance, **kwargs):
    img_filename = instance.picture.name
    pic_compress.delay(os.path.join(settings.MEDIA_URL, img_filename))
