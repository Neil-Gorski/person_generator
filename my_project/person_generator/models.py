from operator import mod
from pyexpat import model
from this import d
from django.db import models
from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlopen
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
    image_url = models.URLField()
    # image_file = models.ImageField(upload_to="photos/male/age/%Y/%m/%d/")
    birthplace = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name + " " + self.surname

    # def get_remote_image(self):
    #     if self.image_url and not self.image_file:
    #         # save image
    #         image_url = self.image_url
    #         img_temp = NamedTemporaryFile(delete=True)
    #         img_temp.write(urlopen(image_url).read())
    #         img_temp.flush()
    #         self.image_file.save("image_%s" % self.pk, File(img_temp))