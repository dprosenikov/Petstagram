from django.test import TestCase, Client

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class PetsDetailsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='mitko2@pro.com', password='123')