from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase

from accounts import views as accounts_views
from accounts.forms import UserRegisterForm

class RegisterTests(TestCase):
    """
    The 'RegisterTests' class test following account registration usages:
        1. Test that the account registration URL is /account/register/.
        2. Test that the /account/register/ URL is handled by function view: register.
        3. Test that registration site is using Django's UserCreationForm, and
            using 'csrfmiddlewaretoken'.
    """
    def setUp(self):
        """
        Get account registratoin site URLs
        GET /account/register/
        """
        url = reverse('register')
        self.response = self.client.get(url)

    def test_register_status_code(self):
        """
        Test that the account registration URL exists.
        GET /account/register/
        """
        self.assertEqual(self.response.status_code, 200)

    def test_register_url_resolves_register_view(self):
        """
        Test that the URL: /account/register/ is executed by
        register view function.
        """
        view = resolve('/account/register/')
        self.assertEqual(view.func, accounts_views.register)

    def test_csrf(self):
        """
        Test that the account registration form used in /account/register/
        is using Cross Site Request Forgery middleware token.
        """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        """
        Test that the form instance used in /account/register/ site is using
        Django's UserCreationForm object.
        """
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserRegisterForm)

class SuccessRegisterTests(TestCase):
    """
    The 'SuccessRegisterTests' class test followings:
        1. Test the new user registration. If registration is successed,
            the user will be redirected to /account/account-activation-sent/
            that display message to check email for confirming account registration.
        2.
    """
    def setUp(self):
        url = reverse('register') # GET /account/register/
        data = {
            'username'  : 'henry',
            'first_name': 'Henry',
            'last_name' : 'Ho',
            'email'     : 'henry@abc.com',
            'password1' : 'abcdef123456',
            'password2' : 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.account_activation_sent_url = reverse('account_activation_sent')

    def test_redirection(self):
        """
        A valid form submission should redirect the user to the
        /account/account-activation-sent/ URL
        """
        self.assertRedirects(self.response, self.account_activation_sent_url)
