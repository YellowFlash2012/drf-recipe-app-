"""tests for models"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """test models"""

    def test_create_user_with_email_success(self):
        """test create a user with email is a success!"""
        email='test@ex.io'
        password='testexio369'

        user=get_user_model().objects.create_user(email=email,password=password)

        self.assertEqual(user.email,email)
        self.assertEqual(user.check_password(password))