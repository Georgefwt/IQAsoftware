from django.db import models

# Create your models here.
class Video(models.Model):
    videoID = models.IntegerField(primary_key=True)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    review_real_number = models.IntegerField(default=0) # total postive review number
    review_uncertain_number = models.IntegerField(default=0) # total uncertain review number
    review_fake_number = models.IntegerField(default=0) # total negative review number

class testcase(models.Model):
    caseID = models.IntegerField(primary_key=True)
    testerSerialNumber = models.IntegerField()
    videoID = models.IntegerField()
    review_result = models.IntegerField() # 2 represent real, 1 represent uncertain, 0 represent fake
