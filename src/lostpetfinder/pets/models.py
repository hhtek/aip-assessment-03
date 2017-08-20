from django.db import models
from django.db.models.signals import pre_save, post_save

from lostpetfinder.utils import unique_slug_generator

# Create your models here.
class LostPet(models.Model):
    PET_CHOICES = (
        ('Cat', 'Cat'),
        ('Dog', 'Dog')
    )
    COLOUR_CHOICES = (
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Brown', 'Brown'),
        ('Calico', 'Calico'),
        ('Chocolate', 'Chocolate'),
        ('Cinnamon', 'Cinnamon'),
        ('Cream', 'Cream'),
        ('Fawn', 'Fawn'),
        ('Ginger', 'Ginger'),
        ('Grey', 'Grey'),
        ('Lilac', 'Lilac'),
        ('Red', 'Red'),
        ('Black', 'Black'),
        ('Tabby', 'Tabby'),
        ('Tortoiseshell', 'Tortoiseshell'),
        ('White', 'White')
    )
    SIZE_CHOICES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Big', 'Big'),
        ('Very Big!', 'Very Big!')
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Unknown')
    )
    YES_NO_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Unknown', 'Unknown')
    )
    STATUS_CHOICES = (
        ('Lost', 'Lost'),
        ('Found', 'Found'),
        ('Registered', 'Registered')
    )
    name            = models.CharField(max_length=120)
    location        = models.CharField(max_length=120, null=True, blank=False)
    pet_type        = models.CharField(max_length=20, choices=PET_CHOICES, null=True, blank=False)
    colour          = models.CharField(max_length=20, choices=COLOUR_CHOICES, null=True)
    age             = models.IntegerField(null=True)
    size            = models.CharField(max_length=20, choices=SIZE_CHOICES, null=True)
    gender          = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    desexed         = models.CharField(max_length=20, choices=YES_NO_CHOICES, null=True, blank=True)
    collar          = models.CharField(max_length=120, null=True, blank=True)
    microchipped    = models.CharField(max_length=20, choices=YES_NO_CHOICES, null=True, blank=True)
    microchipped_no = models.CharField(max_length=120, null=True, blank=True)
    missing_date    = models.DateTimeField(null=True, blank=False)
    status          = models.CharField(max_length=20, default='Registered', choices=STATUS_CHOICES, blank=False)
    description     = models.TextField(max_length=200, null=True, blank=False)
    timestamp       = models.DateTimeField(auto_now_add=True, null=True)
    updated         = models.DateTimeField(auto_now=True, null=True)
    slug            = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving...')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

pre_save.connect(rl_pre_save_receiver, sender=LostPet)
#post_save.connect(rl_post_save_receiver, sender=LostPet)
