from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def getPost(request): 
    return HttpResponse('Getting Post')

def setPost(request): 
    return HttpResponse('Setting Post')
