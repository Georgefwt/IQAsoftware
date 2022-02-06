from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import Video,testcase,User
import random

# policy for selecting video
def first_video_policy():
    total_video_number = Video.objects.count()
    rand_video_ID = random.randint(1,total_video_number)
    return Video.objects.get(videoID=rand_video_ID)

def next_video_policy(tested_video_list):
    total_video_number = Video.objects.count()
    while True:
        rand_video_ID = random.randint(1,total_video_number)
        if(rand_video_ID not in tested_video_list):
            break
    return Video.objects.get(videoID=rand_video_ID)


# Create your views here.

def login_check(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    serial = request.POST.get('serialnumber')
    if (username and email and serial): # make sure all data exist
        try:
            user = User.objects.get(userSerialNumber=serial)
            if (user.user_tested_times == 0):
                user.userName = username
                user.userEmail = email
                user.user_tested_times=1
                user.save()
                response = redirect('/qa/')
                response.set_cookie('serial',serial)
                return response
            return redirect('/login_fail/')
        except Exception as e:
            return redirect('/login_fail/')
    return redirect('/login_fail/')

def login(request):
    return render(request, "login.html")

def login_fail(request):
    return render(request, "loginfail.html")

def assessment(request): # first render assessment page
    if ('serial' in request.COOKIES):
        user_serial = request.COOKIES.get('serial')
        if (User.objects.filter(userSerialNumber=user_serial)):
            video = first_video_policy()
            response = render(request,"assessment.html",{"video":video,"testednumber":0})
            response.set_cookie('v_id',str(video.videoID))
            return response
    return redirect('/login_fail/')

def get_quality(request): # get quality score
    user_serial = request.COOKIES.get('serial')
    user_serial = int(user_serial)

    res = request.GET.get('res')
    res = int(res)
    video_ID = request.GET.get('id')
    video_ID = int(video_ID)

    case = testcase()
    case.testerSerialNumber = user_serial
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
        return JsonResponse({"status":"ok"})
    case.save()
    current_video.save()
    return JsonResponse({"status":"ok"})

def get_next_video(request): # prepare for next video
    video_tested_number = request.GET.get('testednumber')
    video_tested_number = int(video_tested_number)

    vid_cookie = request.COOKIES['v_id']

    if (video_tested_number<10): # temporarily set test number as 10
        tested_video_list = list(map(int, vid_cookie.split('&')))
        video = next_video_policy(tested_video_list)
        response = JsonResponse({"video_caption":video.caption,"video_videoID":video.videoID, \
            "video_url":video.video.url,"status":"ok"})
        response.set_cookie("v_id",vid_cookie+"&"+str(video.videoID))
        return response
    else:
        return JsonResponse({"status":"end"})

def thanksPage(request):
    return render(request, "thanks.html")