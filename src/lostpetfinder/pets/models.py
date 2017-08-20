from django.db import models

# Create your models here.
class LostPet(models.Model):
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
    STATUS_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Unknown', 'Unknown')
    )
    name            = models.CharField(max_length=120)
    pet_type        = models.CharField(max_length=20, choices=(('Cat', 'Cat'), ('Dog', 'Dog')), null=True)
    colour          = models.CharField(max_length=20, choices=COLOUR_CHOICES, null=True)
    age             = models.IntegerField(null=True)
    size            = models.CharField(max_length=20, choices=SIZE_CHOICES, null=True)
    gender          = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    desexed         = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)
    collar          = models.CharField(max_length=120, null=True, blank=True)
    microchipped    = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)
    microchipped_no = models.CharField(max_length=120, null=True, blank=True)
    missing_date    = models.DateTimeField(null=True, blank=False)
    description     = models.TextField(max_length=200, null=True, blank=False)
    timestamp       = models.DateTimeField(auto_now_add=True, null=True)
    updated         = models.DateTimeField(auto_now=True, null=True)
    slug            = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
