from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def features(request):
    return HttpResponse('<h1>vivo has a good features</h1>')

def camera(request):
    return HttpResponse('<h1>It has a high quality camera</h1>')
