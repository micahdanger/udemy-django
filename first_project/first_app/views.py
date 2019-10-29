from django.shortcuts import render
# ADDED THIS
from django.http import HttpResponse
# AND THIS
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    """ OLD STUFF
    my_dict = {
        'insert_me': "Now I am coming from first_app/index.html",
        'insert_content': "HELLO IM FROM FIRSTAPP"}
    """
    return render(request,'first_app/index.html', context=date_dict)
