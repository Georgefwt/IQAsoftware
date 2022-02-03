from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Video,testcase

# Create your views here.
def assessment(request):
    video = Video.objects.all()
    return render(request,"assessment.html",{"video":video})

def get_quality(request):
    res = request.GET.get('res')
    res = int(res)

    case = testcase()
    case.testerSerialNumber = 12345 # temporarily set serial number to 12345
    case.videoID = 0 # temporarily set video id to 0
    if res == 2:
        case.review_result = 2
    elif res == 1:
        case.review_result = 1
    elif res ==0:
        case.review_result = 0
    else:
        return JsonResponse({'status':'ok'})
    case.save()
    return JsonResponse({'status':'ok'})