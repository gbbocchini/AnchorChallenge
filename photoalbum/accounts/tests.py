from django.test import Client, TestCase, override_settings
from django.urls import reverse, reverse_lazy
from django.conf import settings


from .models import GalleryUser


class RegisterTestCase(TestCase):
    print("** Setting up register and Login tests", flush=True)

    def setUp(self):
        self.client = Client()
        self.register_url = reverse_lazy('accounts:register')

    def test_register_ok(self):
        data = {
            'username': 'gabriel', 'password1': 'Bocchini@83', 'password2': 'Bocchini@83',
            'email': 'test@test.com'
        }
        response = self.client.post(self.register_url, data)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed('accounts/register.html')
        print("***Register test ended***", flush=True)


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse_lazy('accounts:login')

    def test_login(self):
        data = {
            'username': 'gabriel', 'password': 'Bocchini@83'
        }
        response = self.client.post(self.login_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('accounts/login.html')
        print("***Login test ended***", flush=True)


