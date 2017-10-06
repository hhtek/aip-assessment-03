
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
