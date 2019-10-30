from django.shortcuts import render
# ADDED THIS
from django.http import HttpResponse
# Create your views here.
from AppTwo.models import Users

def index(request):
    return HttpResponse('<em>My Second App</em>')


def help(request):
    help_dict = {"help_tag": "Help Page"}
    return render(request, "AppTwo/help.html", context=help_dict)


def users(request):
    users_list = Users.objects.order_by('first_name')
    users_dict = {'users': users_list}

    return render(request, 'AppTwo/users.html', context=users_dict)
