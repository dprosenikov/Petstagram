from django.shortcuts import render, redirect

from Petstagram.common.forms import CommentForm
from Petstagram.common.models import Comment
from Petstagram.pets.forms import CreatePetForm
from Petstagram.pets.models import Pet, Like


def list_pets(req):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets
    }
    return render(req, 'pets/pet_list.html', context)


def pet_details(req, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    context = {
        'pet': pet,
        'comment': CommentForm(),
        'comments': pet.comment_set.all()
    }
    return render(req, 'pets/pet_detail.html', context)

def comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        comment = Comment(
            comment=form.cleaned_data['comment'],
            pet = pet,
        )
        comment.save()
    return redirect('pet details', pet.id)

def like_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(pet=pet)
    like.save()
    return redirect('pet details', pk)


def create_pet(request):
    if request.method == 'POST':
        pet = CreatePetForm(request.POST, request.FILES)
        if pet.is_valid():
            pet.save()
            return redirect('list pets')
        else:
            context = {'pet': pet}
            return render(request, 'pets/pet_create.html', context)
    else:
        pet = CreatePetForm()
        context = {
            'pet': pet
        }
        return render(request, 'pets/pet_create.html', context)


def edit_pet(request, pk):
    selected_pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet = CreatePetForm(request.POST, request.FILES, instance=selected_pet)
        if pet.is_valid():
            pet.save()
            return redirect('list pets')
        else:
            context = {'pet': pet}
            return render(request, 'pets/pet_edit.html', context)
    else:
        pet = CreatePetForm(instance=selected_pet)
        context = {
            'pet': pet,
            'selected_pet': selected_pet
        }
        return render(request, 'pets/pet_edit.html', context)


def delete_pet(request, pk):
    selected_pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        selected_pet.delete()
        return redirect('list pets')
    else:
        context = {'pet': selected_pet}
        return render(request, 'pets/pet_delete.html', context)
