from django.db import models

class Lost(models.Model):
    item_id=models.IntegerField(default=0)
    category=models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    lost_time=models.CharField(max_length=200)
    owner=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    status=models.IntegerField(default=0) #0:Finding 1:Found
    img=models.FileField(upload_to='./lost/')
    def __unicode__(self):
        return self.category
