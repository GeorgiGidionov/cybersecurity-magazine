from django.test import TestCase
from django.contrib.auth.models import User

class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = 'testuser'
        cls.user = User.objects.create_user(username=cls.username, password='pass')

    def test_profile_str(self):
        self.assertEqual(str(self.user.profile), f"{self.username}'s profile")