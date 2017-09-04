from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from lostpetfinder.utils import code_generator

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user            = models.OneToOneField(User)
    activated       = models.BooleanField(default=False)
    activation_key  = models.CharField(max_length=120, blank=True, null=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        if not self.activated:
            self.activation_key = code_generator() # generated key
            self.save()
            path_ = reverse('activate', kwargs={'code':self.activation_key})
            subject = 'Activate Account'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = f'Activate your account here: {path_}'
            recipient_list = [self.user.email]
            html_message = f'<p>Activate your account here: {path_}</p>'
            print(html_message)
            sent_mail = send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
                html_message=html_message,
            )
            return sent_mail

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        # default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        # print(default_user_profile)

post_save.connect(post_save_user_receiver, sender=User)
