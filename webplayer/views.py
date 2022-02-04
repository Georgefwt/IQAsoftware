from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import Video,testcase
import random

# policy for selecting video
def first_video_policy():
    total_video_number = Video.objects.count()
    rand_video_ID = random.randint(1,total_video_number)
    print("first rand video ID:{}".format(rand_video_ID))
    return Video.objects.get(videoID=rand_video_ID)

def next_video_policy():
    total_video_number = Video.objects.count()
    rand_video_ID = random.randint(1,total_video_number)
    print("next rand video ID:{}".format(rand_video_ID))
    return Video.objects.get(videoID=rand_video_ID)


# Create your views here.
def assessment(request):
    # video = Video.objects.all()
    video = first_video_policy()
    return render(request,"assessment.html",{"video":video,"testednumber":0})

def get_quality(request):
    res = request.GET.get('res')
    res = int(res)
    video_ID = request.GET.get('id')
    video_ID = int(video_ID)

    case = testcase()
    case.testerSerialNumber = 12345 # temporarily set serial number to 12345
    case.videoID = video_ID
    current_video = Video.objects.get(videoID=video_ID)
    if res == 2:
        case.review_result = 2
        current_video.review_real_number+=1
    elif res == 1:
        case.review_result = 1
        current_video.review_uncertain_number+=1
    elif res ==0:
        case.review_result = 0
        current_video.review_fake_number+=1
    else:
        return JsonResponse({'status':'ok'})
    case.save()
    current_video.save()
    return JsonResponse({'status':'ok'})

def login(request):
    return render(request, "login.html")

def get_next_video(request):
    video_tested_number = request.GET.get('testednumber')
    video_tested_number = int(video_tested_number)
    if (video_tested_number<10): # temporarily set test number as 10
        video = next_video_policy()
        return JsonResponse({"video_caption":video.caption,"video_videoID":video.videoID, \
            "video_url":video.video.url})
    else:
        pass
        # return render(request, "thanks.html")