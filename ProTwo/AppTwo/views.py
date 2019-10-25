from django.shortcuts import render
# ADDED THIS
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    help_dict = {"help_tag": "Help Page"}
    return render(request, "AppTwo/help.html", context=help_dict)
