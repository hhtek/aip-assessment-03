"""
Form classes which are used for accounts application.
    UserRegisterForm: used for new account registration.
    ProfileForm: used to render HTML form with user's extra information
                 including mobile_number,address.
    UserForm: used to redner HTML form with user's information including
              first_name, last_name, email.

"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Profile

class UserRegisterForm(UserCreationForm):
    """
    User registration form extended from UserCreationForm.
    """
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email address.',
    )
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def clean_email(self):
        """
        Check that the email is already registered
        """
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError(f'This email address {email} \
                is already registered with another account and it can not be used!')
        return email.lower()

    def clean_username(self):
        """
        Check if the username is already registered and
        return username with case insensitive
        """
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError(f'This username {username} \
                is already registered and can not be used!')
        return username.lower()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('mobile_number', 'address')

class UserForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email address.',
    )
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        """
        Check that the email is already registered
        """
        pk = self.instance.pk # get pk of requested UserForm
        email = self.cleaned_data.get('email')

        # Get users queryset excluding requested user
        users = User.objects.filter(email__iexact=email).exclude(pk=pk)

        if users:
            raise forms.ValidationError(f'This email address {email} \
                is already registered with another account and it can not be used!')
        return email.lower()
