import email
from django.shortcuts import render

from .app.modul import person_generator
from .models import Person

# Create your views here.
def index(request):
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
        photo=person.photo,
        birthplace=person.place_of_birth)
    p.save()

    return render(request, "person_generator/person_generate.html", {"p": p})