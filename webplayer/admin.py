from django.contrib import admin

# Register your models here.
from .models import Video,testcase

admin.site.site_header = 'Video manager'  # config headererer
admin.site.site_title = 'videomanager'

admin.site.register(Video)
admin.site.register(testcase)