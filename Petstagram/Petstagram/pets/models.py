import os
from os.path import join

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Pet(models.Model):
    TYPE_DOG = 'dog'
    TYPE_CAT = 'cat'
    TYPE_PARROT = 'parrot'
    TYPES = ((TYPE_DOG, 'Dog'), (TYPE_CAT, 'Cat'), (TYPE_PARROT, 'Parrot'))
    type = models.CharField(
        max_length=6,
        choices=TYPES
    )
    name = models.CharField(
        max_length=6
    )
    age = models.PositiveIntegerField(
    )
    description = models.TextField(
    )
    image = models.ImageField(
        upload_to='images/pets'
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    # # delete the image that is edited/replaced
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     db_pet = Pet.objects.get(pk=self.id)
    #     image_path = join(settings.MEDIA_ROOT, str(db_pet.image))
    #     os.remove(image_path)
    #     return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
