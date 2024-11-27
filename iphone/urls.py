from iphone.views import *
from django.urls import path

urlpatterns=[
    path('storage/',storage,name='storage'),
    path('security/',security,name='')
]