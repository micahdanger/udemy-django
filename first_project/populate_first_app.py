import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import sys
sys.path.append('/Users/micahbeckman/codeprojects/udemy-django/djangoenv/lib/python3.7/site-packages')

import django
django.setup()

## FAKE POP script
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    # THE [0] TAKES THE FIRST ELEMENT IN THE TUPLE
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        # GET THE TOPIC FOR THE ENTRY
        top = add_topic()

        # CREATE THE FAKE DATA FOR THAT ENTRY
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # CREATE THE NEW WEBPAGE ENTRY
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # CREATE A FAKE ACCESS RECORD FOR THAT WEBPAGE
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
