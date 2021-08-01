from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from Petstagram.accounts.forms import LoginForm, RegisterForm, ProfileForm
from Petstagram.accounts.models import Profile
from Petstagram.pets.models import Pet


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    user_pets = Pet.objects.filter(user_id=request.user.id)
    context = {
        'form': form,
        'pets': user_pets,
        'profile': profile
    }
    return render(request, 'accounts/user_profile.html', context)
