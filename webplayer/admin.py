from django.contrib import admin

# Register your models here.
from .models import Video,testcase,User

admin.site.site_header = 'Video manager'  # config headererer
admin.site.site_title = 'videomanager'

class VideoInfoAdmin(admin.ModelAdmin):
    list_display=['videoID','caption','review_real_number','review_uncertain_number','review_fake_number']
    search_fields = ['videoID','caption']

class testcaseInfoAdmin(admin.ModelAdmin):
    list_display=['caseID','testerSerialNumber','videoID','review_result']
    search_fields = ['videoID','testerSerialNumber','review_result']

class UserInfoAdmin(admin.ModelAdmin):
    list_display=['userID','userSerialNumber','userName','userEmail','user_tested_times']
    search_fields = ['userSerialNumber','userName','userEmail']

admin.site.register(Video,VideoInfoAdmin)
admin.site.register(testcase,testcaseInfoAdmin)
admin.site.register(User,UserInfoAdmin)