from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from Petstagram.accounts.models import Profile
from Petstagram.pets.models import Pet

UserModel = get_user_model()


class ProfileDetailsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='mitko2@pro.com', password='123')

    def test_get_when_loggedin(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile'))

        pets = list(response.context['pets'])
        self.assertListEqual(pets, [])
        profile = response.context['profile']
        self.assertEqual(self.user.id, profile.user_id)

    def test_get_when_loggedin_withPets(self):
        self.client.force_login(self.user)

        pet = Pet.objects.create(
            name='Pesho',
            description='Kuche 1',
            age=1,
            image='path/to/image.png',
            type=Pet.TYPE_DOG,
            user=self.user
        )
        response = self.client.get(reverse('profile'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([pet], list(response.context['pets']))

    # def test_postdetails_whenuserchangesimage(self):
    #     path_to_image = 'path/to/image.png'
    #     self.client.force_login(self.user)
    #
    #     response = self.client.post(reverse('profile'), data={'profile_image': path_to_image})
    #
    #     self.assertEqual(302, response.status_code)
    #
    #     profile = Profile.objects.get(pk=self.user.id)
    #     self.assertEqual(path_to_image, profile.profile_image.path)
