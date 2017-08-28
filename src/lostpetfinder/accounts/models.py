from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user        = models.OneToOneField(User)
    activated   = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        print('Activation')
        pass

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        print(profile)
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        print(default_user_profile)

post_save.connect(post_save_user_receiver, sender=User)
