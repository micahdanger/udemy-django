from django.shortcuts import render
# ADDED THIS
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {
        'insert_me': "Now I am coming from first_app/index.html",
        'insert_content': "HELLO IM FROM FIRSTAPP"}

    return render(request,'first_app/index.html', context=my_dict)
