from operator import mod
from pyexpat import model
from this import d
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def only_int(value):
    if value.isdigit() == False:
        raise ValidationError('Phonenumber contains characters')



class Person(models.Model):
    GENDER = [ ("male", "Male"), ("female", "Female")]
    gender = models.CharField(max_length=10, choices=GENDER)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    birthday_date = models.DateTimeField()
    email = models.EmailField()
    job = models.CharField(max_length=100)
    weight = models.IntegerField()
    phone = models.CharField(max_length=12, validators=[only_int])
    photo = models.CharField(max_length=200)
    birthplace = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + " " + self.surname
