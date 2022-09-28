from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_all_persons, name="home"),
    path("new/", views.create_random_person, name="new"),
    path("api/", views.PersonsView.as_view(), name="api_persons"),
    path("api/<int:pk>/", views.PersonViewAPI.as_view(), name="api_person"),
]
