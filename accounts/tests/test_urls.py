from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import signup_view, login_view, logout_view

class AccountURLTest(SimpleTestCase):

    def test_signup_url(self):
        url = reverse('accounts:signup')
        self.assertEqual(resolve(url).func, signup_view)

    def test_login_url(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func, login_view)

    def test_logout_url(self):
        url = reverse('accounts:logout')
        self.assertEqual(resolve(url).func, logout_view)
    
