from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class AccountsTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')

    def test_signup_view_get(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_signup_view_post_valid(self):
        data = {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        response = self.client.post(reverse('accounts:signup'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertRedirects(response, reverse('articles:list'))

    def test_signup_view_post_invalid(self):
        data = {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'differentpassword'
        }
        response = self.client.post(reverse('accounts:signup'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='newuser').exists())
        self.assertTemplateUsed(response, 'accounts/signup.html')
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_login_view_get(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(response.context['form'], AuthenticationForm)

    def test_login_view_post_valid(self):
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        response = self.client.post(reverse('accounts:login'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('articles:list'))

    def test_login_view_post_invalid(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(reverse('accounts:login'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(response.context['form'], AuthenticationForm)

    def test_login_view_post_with_next(self):
        data = {
            'username': 'testuser',
            'password': 'password123',
            'next': reverse('articles:create')
        }
        response = self.client.post(reverse('accounts:login'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('articles:create'))

    def test_logout_view_post(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('articles:list'))

