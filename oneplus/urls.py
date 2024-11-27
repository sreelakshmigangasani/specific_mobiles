from oneplus.views import *
from django.urls import path

urlpatterns=[
    path('battery/',battery,name='battery'),
    path('charging/',charging,name='charging'),
]