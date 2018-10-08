import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd2Proj.settings')

import django
django.setup()

##Fake population script
from d2App.models import User
from faker import Faker

#import random
fakegen = Faker()
#emails = ['gmail','yahoo','aol','msn']

def populate(n=5):
    for entry in range(n):
        #create fake data for that entry
        fake_firstName = fakegen.first_name()
        fake_lastName = fakegen.last_name()
        fake_email = fakegen.free_email()

        user = User.objects.get_or_create(firstName=fake_firstName, lastName=fake_lastName, email=fake_email)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('population complete!')
