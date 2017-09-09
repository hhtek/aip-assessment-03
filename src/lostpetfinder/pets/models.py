import os
from django.conf import settings
from django.core.urlresolvers import reverse, resolve
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone

from django.core.files.storage import FileSystemStorage


from lostpetfinder.utils import unique_slug_generator

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        dir_name, file_name = os.path.split(name)
        file_root, file_ext = os.path.splitext(file_name)
        if file_name:
            self.delete(name)
            print("Deleted old file %s" %name)
        return name

def file_upload_location(instance, filename):
    """
    Function used to get the location to store the uploaded file.
    """
    file_root, file_ext = os.path.splitext(filename)
    file_name = '%s%s' %(instance.slug, file_ext) # e.g. henrys-cat.jpg
    print(file_name)
    return os.path.join(instance._meta.app_label, file_name).lower()

class Pet(models.Model):
    """
    Pet data model to store pet details
    """
    # Pre-defined TUPLES
    # Tubple declaration with all CAPITAL LETTERS.
    PET_CHOICES = (
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
        ('Rabbit','Rabbit'),
        ('Pig','Pig'),
        ('Bird','Bird'),
        ('Ferret','Ferret'),
        ('Horse','Horse'),
        ('Sheep','Sheep'),
        ('Turtle','Turtle'),
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
        ('White', 'White'),
    )
    SIZE_CHOICES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Big', 'Big'),
        ('Very Big!', 'Very Big!'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Unknown'),
    )
    YES_NO_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Unknown', 'Unknown'),
    )
    STATUS_CHOICES = (
        ('Lost', 'Lost'),
        ('Found', 'Found'),
        ('Registered', 'Registered'),
    )


    # Fields definition
    owner           = models.ForeignKey(settings.AUTH_USER_MODEL) # Owner association
    name            = models.CharField(max_length=120)
    location        = models.CharField(max_length=120, null=True, blank=False)
    pet_type        = models.CharField(max_length=20, choices=PET_CHOICES,
                        null=True, blank=False)
    colour          = models.CharField(max_length=20, choices=COLOUR_CHOICES,
                        null=True)
    age             = models.IntegerField(null=True)
    size            = models.CharField(max_length=20, choices=SIZE_CHOICES,
                        null=True)
    gender          = models.CharField(max_length=20, choices=GENDER_CHOICES,
                        null=True)
    desexed         = models.CharField(max_length=20, choices=YES_NO_CHOICES,
                        null=True, blank=True)
    collar          = models.CharField(max_length=120, null=True, blank=True)
    microchipped    = models.CharField(max_length=20, choices=YES_NO_CHOICES,
                        null=True, blank=True)
    microchipped_no = models.CharField(max_length=120, null=True, blank=True)
    missing_date    = models.DateTimeField(null=True, blank=False)
    status          = models.CharField(max_length=20, default='Registered',
                        choices=STATUS_CHOICES, blank=False)
    description     = models.TextField(max_length=200, null=True, blank=False)
    pet_image       = models.ImageField(upload_to=file_upload_location, storage=OverwriteStorage(), null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True, null=True)
    updated         = models.DateTimeField(auto_now=True, null=True)
    slug            = models.SlugField(null=True, blank=True)

    # Ordering item by updated aDeletingnd timestamp by descending order
    class Meta:
        ordering = ['-updated', '-timestamp']

    # Display Pet object with its name field
    def __str__(self):
        return self.name

    # Get absolute URL of pets:detail view
    def get_absolute_url(self):
        return reverse('pets:detail', kwargs={'slug': self.slug})

    # title: aka of name field to be used with unique_slug_generator()
    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Pet)
#post_save.connect(rl_post_save_receiver, sender=Pet)

class Comment(models.Model):
    post = models.ForeignKey(Pet)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
