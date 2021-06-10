from django.shortcuts import render, redirect

from Petstagram.pets.models import Pet, Like


def list_pets(req):
    all_pets = Pet.objects.all()
    context = {
        'pets' : all_pets
    }
    return render(req,'pets/pet_list.html', context)

def pet_details(req, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    context = {
        'pet' : pet
    }
    return render(req,'pets/pet_detail.html', context)

def like_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(pet=pet)
    like.save()
    return redirect('pet details', pk)
