from tokenize import blank_re
from django.db import models

# Create your models here.
class Video(models.Model):
    videoID = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    review_real_number = models.IntegerField(default=0) # total postive review number
    review_uncertain_number = models.IntegerField(default=0) # total uncertain review number
    review_fake_number = models.IntegerField(default=0) # total negative review number

class testcase(models.Model):
    caseID = models.AutoField(primary_key=True)
    testerSerialNumber = models.CharField(max_length=100)
    videoID = models.IntegerField()
    review_result = models.IntegerField() # 2 represent real, 1 represent uncertain, 0 represent fake

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userSerialNumber = models.CharField(max_length=100) # serial number for login
    userName = models.CharField(max_length=16,blank=True,null=True)
    userEmail = models.CharField(max_length=30,blank=True,null=True)
    user_tested_times = models.IntegerField(default=0)
