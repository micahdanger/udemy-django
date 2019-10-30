import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import sys
sys.path.append('/Users/micahbeckman/codeprojects/udemy-django/ProTwo/djangoenv_ProTwo/lib/python3.7/site-packages')

import django
django.setup()

# FAKE POP SCRIPT
import random
from AppTwo.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for element in range(N):

        # CREATE FAKE NAMES AND EMAIL
        fake_name = fakegen.name()
        fake_first_name = fake_name.split(" ")[0]
        fake_last_name = fake_name.split(" ")[1]
        fake_email = fakegen.email()
        print(fake_name + ' / ' + fake_email)

        name = Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
