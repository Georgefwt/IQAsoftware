from unicodedata import name
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
    n = total_video_number
    while n>0:
        rand_video_ID = random.randint(1,total_video_number)
        if(rand_video_ID not in tested_video_list):
            break
        n -= 1
    return Video.objects.get(videoID=rand_video_ID)

def next_video_policy_large(tested_video_list):
    total_video_number = Video.objects.count()
    batchsize = total_video_number//30
    n = batchsize+1
    lastv_id = tested_video_list[-1]
    while n>0:
        rand_video_ID = (random.randint(batchsize*((lastv_id-1)//batchsize+1)+1, \
            batchsize*((lastv_id-1)//batchsize+2))-1)%total_video_number + 1
        if(rand_video_ID not in tested_video_list):
            break
        n -= 1
    return Video.objects.get(videoID=rand_video_ID)

# Create your views here.

def login_check(request):
    username = request.POST.get('username').replace(" ","").replace("\t","")
    email = request.POST.get('email').replace(" ","").replace("\t","")
    serial = request.POST.get('serialnumber').replace(" ","").replace("\t","")
    if (username and email and serial): # make sure all data exist
        try:
            user = User.objects.get(userSerialNumber=serial)
            if (user.user_tested_times == 0):
                if user.userName is None:
                    user.userName = username
                else:
                    print(user.userName)
                    if (user.userName!=username):
                        return redirect('loginfailpage')
                user.userEmail = email
                user.save()
                response = redirect('notice')
                response.set_cookie('serial',serial)
                response.delete_cookie('v_id')
                return response
            return redirect('loginfailpage')
        except Exception as e:
            return redirect('loginfailpage')
    return redirect('loginfailpage')

def login(request):
    return render(request, "login.html")

def login_fail(request):
    return render(request, "loginfail.html")

def preassessment(request):
    if ('serial' in request.COOKIES):
        return render(request, "preassessment.html")
    return redirect('loginfailpage')
    

def assessment(request): # first render assessment page
    if ('serial' in request.COOKIES):

        user_serial = request.COOKIES.get('serial')
        if (User.objects.filter(userSerialNumber=user_serial)):

            if ('v_id' in request.COOKIES): # deal with refresh situration
                vid_cookie = request.COOKIES['v_id']
                tested_video_list = list(map(int, vid_cookie.split('&')))
                video = Video.objects.get(videoID=tested_video_list[-1])
                response = render(request,"assessment.html",{"video":video,"testednumber":(len(tested_video_list)-1)})
                response.set_cookie('v_id',vid_cookie)
                return response
            else: # first enter, not refresh
                video = first_video_policy()
                response = render(request,"assessment.html",{"video":video,"testednumber":0})
                response.set_cookie('v_id',str(video.videoID))
                return response
    return redirect('loginfailpage')

def notice(request):
    return render(request, "notice.html")

def get_quality(request): # get quality score
    try:
        user_serial = request.COOKIES.get('serial')
        user = User.objects.get(userSerialNumber=user_serial)
        if user is None:
            return JsonResponse({"status":"fail"})
        if user.user_tested_times > 30:
            return JsonResponse({"status":"fail"})
        dim1 = int(request.GET.get('dim1'))
        dim2 = int(request.GET.get('dim2'))
        dim3 = int(request.GET.get('dim3'))
        video_ID = int(request.GET.get('id'))

        current_video = Video.objects.get(videoID=video_ID)
        case = testcase()
        case.testerSerialNumber = user_serial
        case.videoID = video_ID
        if (dim1!=-1 and dim2!=-1 and dim3!=-1):
            case.review_d1 = dim1
            case.review_d2 = dim2
            case.review_d3 = dim3

            if dim1 == 2:
                current_video.review_d1r2+=1
            elif dim1 == 1:
                current_video.review_d1r1+=1
            elif dim1 ==0:
                current_video.review_d1r0+=1
            else:
                return JsonResponse({"status":"fail"})
            if dim2 == 2:
                current_video.review_d2r2+=1
            elif dim2 == 1:
                current_video.review_d2r1+=1
            elif dim2 ==0:
                current_video.review_d2r0+=1
            else:
                return JsonResponse({"status":"fail"})
            if dim3 == 2:
                current_video.review_d3r2+=1
            elif dim3 == 1:
                current_video.review_d3r1+=1
            elif dim3 ==0:
                current_video.review_d3r0+=1
            else:
                return JsonResponse({"status":"fail"})

            case.save()
            current_video.save()
            user.user_tested_times+=1
            user.save()
            return JsonResponse({"status":"ok"})
        return JsonResponse({"status":"fail"})
    except:
        return JsonResponse({"status":"fail"})


def get_next_video(request): # prepare for next video
    video_tested_number = request.GET.get('testednumber')
    video_tested_number = int(video_tested_number)

    vid_cookie = request.COOKIES['v_id']

    if (video_tested_number<30): # set test number as 30
        try:
            tested_video_list = list(map(int, vid_cookie.split('&')))
            video = next_video_policy_large(tested_video_list)
            response = JsonResponse({"video_caption":video.caption,"video_videoID":video.videoID, \
                "video_url":video.video.url,"status":"ok"})
            response.set_cookie("v_id",vid_cookie+"&"+str(video.videoID))
            return response
        except:
            return JsonResponse({"status":"error"})
    else:
        try:
            user_serial = request.COOKIES.get('serial')
            user = User.objects.get(userSerialNumber=user_serial)
            user.user_tested_times=100 # when test finished, make user tested times as 100
            user.save()
            return JsonResponse({"status":"end"})
        except:
            return JsonResponse({"status":"error"})

def thanksPage(request):
    return render(request, "thanks.html")