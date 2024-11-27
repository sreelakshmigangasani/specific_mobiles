from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def battery(request):
    return HttpResponse('<h1>oneplus has a long battery life</h1>')

def charging(request):
    return HttpResponse('<h1>Fast cahrging capability</h1>')
