from django.shortcuts import render
# ADDED THIS
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<em>My Second App</em>')