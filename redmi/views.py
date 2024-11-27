from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def storage(request):
    return HttpResponse('<h1>redmi has a 128gb storage</h1>')

def price(request):
    return HttpResponse('<h1>affordable price</h1>')
