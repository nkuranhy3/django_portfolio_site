from django.shortcuts import render

from django.http import  HttpResponse

from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/index.html', {"jobs": jobs })


def about(request):
    return render(request, 'jobs/about.html')


