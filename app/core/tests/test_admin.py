from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(

            email='admin@co.com',
            password='1234',
            id=uuid.uuid4()
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='a@ds.com',
            password='1234',
            id=uuid.uuid4()
        )

    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_user_create_page(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
