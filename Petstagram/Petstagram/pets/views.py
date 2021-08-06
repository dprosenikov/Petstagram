from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, FormView, ListView, CreateView, UpdateView, DeleteView

from Petstagram.common.forms import CommentForm
from Petstagram.common.models import Comment
from Petstagram.pets.forms import CreatePetForm
from Petstagram.pets.models import Pet, Like


class PetsListView(ListView):
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'
    model = Pet


# def list_pets(req):
#     all_pets = Pet.objects.all()
#     context = {
#         'pets': all_pets
#     }
#     return render(req, 'pets/pet_list.html', context)


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = context['pet']
        pet.likes_count = pet.like_set.count()
        is_owner = pet.user == self.request.user
        is_liked = pet.like_set.filter(user_id=self.request.user.id).first()
        context['comment'] = CommentForm()
        context['comments'] = pet.comment_set.all()
        context['is_owner'] = is_owner
        context['is_liked'] = is_liked
        return context


# def pet_details(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     pet.likes_count = pet.like_set.count()
#     is_owner = pet.user == request.user
#     is_liked = pet.like_set.filter(user_id=request.user.id).first()
#     context = {
#         'pet': pet,
#         'comment': CommentForm(),
#         'comments': pet.comment_set.all(),
#         'is_owner': is_owner,
#         'is_liked': is_liked
#     }
#     return render(request, 'pets/pet_detail.html', context)


@login_required
def comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        comment = Comment(
            comment=form.cleaned_data['comment'],
            pet=pet,
            user=request.user
        )
        comment.save()
    return redirect('pet details', pet.id)


@login_required
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    is_liked = pet.like_set.filter(user_id=request.user.id).first()
    if is_liked:
        is_liked.delete()
    else:
        like = Like(pet=pet, user=request.user)
        like.save()
    return redirect('pet details', pk)


class PetCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pets/pet_create.html'
    model = Pet
    fields = ('type', 'name', 'age', 'description', 'image')
    success_url = reverse_lazy('list pets')

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)


# @login_required
# def create_pet(request):
#     if request.method == 'POST':
#         pet = CreatePetForm(request.POST, request.FILES)
#         if pet.is_valid():
#             form = pet.save(commit=False)
#             form.user = request.user
#             form.save()
#             return redirect('list pets')
#         else:
#             context = {'pet': pet}
#             return render(request, 'pets/pet_create.html', context)
#     else:
#         pet = CreatePetForm()
#         context = {
#             'pet': pet
#         }
#         return render(request, 'pets/pet_create.html', context)


class PetEditView(LoginRequiredMixin, UpdateView):
    model = Pet
    template_name = 'pets/pet_edit.html'
    form_class = CreatePetForm
    success_url = reverse_lazy('list pets')


# @login_required
# def edit_pet(request, pk):
#     selected_pet = Pet.objects.get(pk=pk)
#     if request.method == 'POST':
#         pet = CreatePetForm(request.POST, request.FILES, instance=selected_pet)
#         if pet.is_valid():
#             pet.save()
#             return redirect('list pets')
#         else:
#             context = {'pet': pet}
#             return render(request, 'pets/pet_edit.html', context)
#     else:
#         pet = CreatePetForm(instance=selected_pet)
#         context = {
#             'pet': pet,
#             'selected_pet': selected_pet
#         }
#         return render(request, 'pets/pet_edit.html', context)


class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet_delete.html'
    success_url = reverse_lazy('list pets')

# @login_required
# def delete_pet(request, pk):
#     selected_pet = Pet.objects.get(pk=pk)
#     if request.method == 'POST':
#         selected_pet.delete()
#         return redirect('list pets')
#     else:
#         context = {'pet': selected_pet}
#         return render(request, 'pets/pet_delete.html', context)
