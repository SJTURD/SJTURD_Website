from django.db import models

class Volunteer(models.Model):
	volunteer_id=models.IntegerField(default=0)
	name=models.CharField(max_length=200)
	password=models.CharField(max_length=200)

class LostItem(models.Model):
	item_id=models.IntegerField(default=0)
	category=models.CharField(max_length=200)
	description=models.CharField(max_length=400)
	lost_time=models.CharField(max_length=200)
	owner=models.CharField(max_length=200)
	contact=models.CharField(max_length=200)
	STATUS=(
		(0,'Finding'),
		(1,'Found'),
		(2,'OW')
	)
