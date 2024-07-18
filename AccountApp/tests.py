from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('AccountApp:ViewLogin')
        self.home_url = reverse('HomeApp:ViewHome')
        self.username = 'admin'
        self.password = 'admin'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AccountApp/LoginView.html')

    def test_login_view_POST_valid(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, self.home_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_POST_invalid(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AccountApp/LoginView.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)
