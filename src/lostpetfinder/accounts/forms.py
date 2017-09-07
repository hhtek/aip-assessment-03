from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    """
    Signup form estended from UserCreationForm used for user registration.
    """
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

    # Check if the email is already registered
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email address %s is already registered and it can not be used!" % email)
        return email
