from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTestClass(TestCase):
    def test_user_created(self):
        user = get_user_model().objects.create_user(
            email='hello@as.com',
            password="asdf"
        )
        self.assertEqual(user.email, 'hello@as.com')
        self.assertTrue(user.check_password('asdf'))

    def test_email_normalised(self):
        email = 'bush@Peace.UI'
        pwd = '123'
        user = get_user_model().objects.create_user(
            email,
            pwd
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass1234')

    def test_new_superuser(self):
        user = get_user_model().objects.create_superuser('ad@sd.com', '1234')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
