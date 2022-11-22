import email
from django.shortcuts import render

from .app.modul import person_generator
from .models import Person
from rest_framework import generics, permissions
from .serializers import PersonSerializer
import random


# Create your views here.
def create_random_person(request):
    person = person_generator.Person()
    p = Person(gender=person.gender,
        name=person.name,
        surname=person.surname,
        age=person.age,
        birthday_date=person.birthday_date,
        email=person.email,
        job=person.job,
        weight=person.weight,
        phone=person.phone,
        image_url=person.photo,
        birthplace=person.place_of_birth)
    p.save()
 

    return render(request, "person_generator/new_person_generate.html", {"p": p})

def list_all_persons(request):
    persons = list(Person.objects.all())
    persons = random.sample(persons, 24)
    return render(request, "person_generator/person_list.html", {"persons": persons})

class PersonsView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = ()

class PersonViewAPI(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = ()
    lookup_url_kwarg = "pk"