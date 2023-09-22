import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','advcbv.settings')

import django
# Import settings
django.setup()

import random
from basic_app.models import School, Student
from faker import Faker
from faker_education import SchoolProvider


fakegen = Faker()
fakegen.add_provider(SchoolProvider)

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        #Fake data for school
        fake_school_name = fakegen.school_name()
        fake_principal_name = fakegen.name()
        fake_school_address = fakegen.address().replace('\n', ' ')

        #Fake data for student
        fake_student_name = fakegen.name()
        fake_student_age = random.randint(6, 12)

        # Create new School Entry
        school = School.objects.get_or_create(name=fake_school_name,
                                          principal=fake_principal_name,
                                          location=fake_school_address)[0]

        # Create new Student Entry
        student = Student.objects.get_or_create(name=fake_student_name,
                                          age=fake_student_age,
                                          school=school)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(40)
    print('Populating Complete')
