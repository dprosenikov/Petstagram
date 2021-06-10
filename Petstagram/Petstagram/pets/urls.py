from django.urls import path

from Petstagram.pets.views import list_pets

urlpatterns = [
    path('', list_pets, name='list pets')
]