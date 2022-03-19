from tokenize import blank_re
from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Video(models.Model):
    videoID = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    review_d1r4 = models.IntegerField(default=0)
    review_d1r3 = models.IntegerField(default=0)
    review_d1r2 = models.IntegerField(default=0)
    review_d1r1 = models.IntegerField(default=0)
    review_d1r0 = models.IntegerField(default=0)

    review_d2r2 = models.IntegerField(default=0)
    review_d2r1 = models.IntegerField(default=0)
    review_d2r0 = models.IntegerField(default=0)

class testcase(models.Model):
    caseID = models.AutoField(primary_key=True)
    testerSerialNumber = models.CharField(max_length=100)
    videoID = models.IntegerField()
    review_d1 = models.IntegerField() #dimension1
    review_d2 = models.IntegerField() #dimension2

    # time = models.TimeField(auto_now_add=True)
    test_time = models.DateTimeField('add time',default = timezone.now)

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userSerialNumber = models.CharField(max_length=100) # serial number for login
    userName = models.CharField(max_length=16,blank=True,null=True)
    userEmail = models.CharField(max_length=30,blank=True,null=True)
    user_tested_times = models.IntegerField(default=0)
