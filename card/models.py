from django.db import models


class Card(models.Model):
    user = models.ForeignKey('user.UserExt', on_delete=models.CASCADE, default=1)

    student_id = models.CharField(max_length=32, blank=False, null=False, default='-1')
    name = models.CharField(max_length=128, blank=False, null=False, default='error')
    lfoffice = models.ForeignKey('main.LFOffice', on_delete=models.SET_DEFAULT, default=1)

    date = models.DateTimeField(auto_now_add=True)

    paired = models.BooleanField(default=False)
