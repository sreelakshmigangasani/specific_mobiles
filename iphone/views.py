from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def storage(request):
    return HttpResponse('<h1>iphone has a high quality camera</h1>')

def security(request):
    return HttpResponse('<h1>Highly secured</h1>')