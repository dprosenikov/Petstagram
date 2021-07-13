import os
from os.path import join

from django import forms
from django.conf import settings

from Petstagram.pets.models import Pet


class CreatePetForm(forms.ModelForm):
    type = forms.ChoiceField(
        choices=[("dog", "dog"), ("cat", "cat"), ("parrot", "parrot")],
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            },
        )
    )

    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    age = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'number'
            }
        )
    )

    image = forms.ImageField(
        required=True,
        # widget=forms.FileField(
        #     attrs={
        #         'class': 'form-control'
        #     }
        # )
    )

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2'
            }
        )
    )

    #delete the image that is edited/replaced
    def save(self, commit=True):
        db_pet = Pet.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_pet.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Pet
        fields = ('type', 'name', 'age', 'description', 'image')