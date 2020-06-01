import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','demo_project.settings')

import django
django.setup()

import random
from demo_app.models import Members,Activity
from faker import Faker

fakegen =Faker()
user_id=['W1245','X7874','k8798']
name=['maria','kishore','kiran']
timezone=['india/kolkatha','karnataka/bangalore']


def add_id():
    userid = Members.objects.get_or_create(id=random.choice(user_id))[0]
    userid.save()
    return userid

def add_name():
    NAME=Members.objects.get_or_create(real_name=random.choice(name))[0]
    NAME.save()
    return NAME

def add_tz():
    TZ=Members.objects.get_or_create(tz=random.choice(timezone))[0]
    TZ.save()
    return TZ

def populate(N=5):
    for entry in range(N):

        Userid=add_id()
        Name=add_name()
        TimeZone=add_tz()

        member=Members.objects.get_or_create(id=Userid,real_name=Name,tz=TimeZone)[0]



        #activity_periods=Activity.objects.get_or_create(starttime=fake_start_date,endtime=fake_end_date)[0]
if __name__=='__main__':
    print("population script")
    populate(10)
    print("populating Complete")
