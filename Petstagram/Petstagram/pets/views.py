from django.shortcuts import render

from Petstagram.pets.models import Pet


def list_pets(req):
    all_pets = Pet.objects.all()
    context = {
        'pets' : all_pets
    }
    return render(req,'pets/pet_list.html', context)

def pet_details(req, pk):
    pass
