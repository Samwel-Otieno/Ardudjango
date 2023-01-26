from django.shortcuts import render, redirect
from .functions import *
# Create your views here.

def index(request):
    if request.method=='POST':
        streamer()   
    return render(request, 'ardudjango/index.html')