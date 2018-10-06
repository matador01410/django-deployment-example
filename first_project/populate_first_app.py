import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## FALKE POP SCRIPT
import random
from first_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for entry
        top = add_topic()

        # Create the fake data fo that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email_address = fakegen.email()
        # Create the new webpage entry

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webpage
        accessrecor = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

        # Create a fake user name
        users = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email_address=fake_email_address)


if __name__ == '__main__':
    print('population script')
    populate(20)
    print('Population complete')