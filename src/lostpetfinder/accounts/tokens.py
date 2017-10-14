"""
Custom activation token generator which is extended from
PasswordResetTokenGenerator

Reference:
https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html#sign-up-with-confirmation-mail
"""
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """
    Unique token generator extended from PasswordResetTokenGenerator to
    confirm user's registered email address.
    """
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.email)
        )

account_activation_token = AccountActivationTokenGenerator()
