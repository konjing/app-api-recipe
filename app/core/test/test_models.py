from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email for new user is normalized"""
        email = 'test@EXAMPLE.cOm'
        user = get_user_model().objects.create_user(email, 'pass123')

        self.assertEqual(user.email, 'test@example.com')

    def test_new_user_invalid_email(self):
        """Test new user no input email """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass123')

    def test_create_new_superuser(self):
        """Test create superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'pass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
