from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("new", views.create_random_person, name="home"),
]
