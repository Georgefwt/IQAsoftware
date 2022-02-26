from tokenize import blank_re
from django.db import models

# Create your models here.
class Video(models.Model):
    videoID = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    review_d1r2 = models.IntegerField(default=0)
    review_d1r1 = models.IntegerField(default=0)
    review_d1r0 = models.IntegerField(default=0)
    review_d2r2 = models.IntegerField(default=0)
    review_d2r1 = models.IntegerField(default=0)
    review_d2r0 = models.IntegerField(default=0)
    review_d3r2 = models.IntegerField(default=0)
    review_d3r1 = models.IntegerField(default=0)
    review_d3r0 = models.IntegerField(default=0)

class testcase(models.Model):
    caseID = models.AutoField(primary_key=True)
    testerSerialNumber = models.CharField(max_length=100)
    videoID = models.IntegerField()
    review_d1 = models.IntegerField() #dimension1, 2 represent natural, 1 represent uncertain, 0 represent unatural
    review_d2 = models.IntegerField() #dimension2, 2 represent fluent, 1 represent uncertain, 0 represent unfluent
    review_d3 = models.IntegerField() #dimension3, 2 represent sharp, 1 represent uncertain, 0 represent unsharp

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userSerialNumber = models.CharField(max_length=100) # serial number for login
    userName = models.CharField(max_length=16,blank=True,null=True)
    userEmail = models.CharField(max_length=30,blank=True,null=True)
    user_tested_times = models.IntegerField(default=0)
