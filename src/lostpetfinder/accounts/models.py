from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number   = models.CharField(max_length=10, null=True, blank=True)
    address         = models.CharField(max_length=300, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    instance.profile.save() # save_user_profile
