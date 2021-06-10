from django.db import models


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
    image_url = models.URLField(
    )


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
