from django.contrib import admin

# Register your models here.
from .models import Video,testcase,User

admin.site.site_header = 'Video manager'  # config headererer
admin.site.site_title = 'videomanager'

class VideoInfoAdmin(admin.ModelAdmin):
    list_display=['videoID','caption']
    search_fields = ['videoID','caption']

class testcaseInfoAdmin(admin.ModelAdmin):
    list_display=['caseID','testerSerialNumber','videoID','review_d1','test_time']
    search_fields = ['videoID','testerSerialNumber']

class UserInfoAdmin(admin.ModelAdmin):
    list_display=['userID','userSerialNumber','userName','userEmail','user_tested_times']
    search_fields = ['userSerialNumber','userName','userEmail']

admin.site.register(Video,VideoInfoAdmin)
admin.site.register(testcase,testcaseInfoAdmin)
admin.site.register(User,UserInfoAdmin)