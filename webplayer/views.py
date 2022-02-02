from django.shortcuts import render
from .models import Video

# Create your views here.
def assessment(request):
    video = Video.objects.all()
    return render(request,"assessment.html",{"video":video})