from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def authen(request):
    return render(request,'authen.html')

def adding(request):
    return render(request, 'adding.html')