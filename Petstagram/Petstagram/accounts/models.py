from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
from Petstagram.accounts.managers import PetstagramUserManager


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    is_staff = models.BooleanField(default=False)
    objects = PetstagramUserManager()
    date_joined = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    profile_image = models.ImageField(upload_to='images/profiles')
    user = models.OneToOneField(PetstagramUser, on_delete=models.CASCADE, primary_key=True)

from .signals import *