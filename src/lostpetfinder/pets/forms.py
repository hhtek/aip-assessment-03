"""
File name: forms.py
Description: Django form classes which are used with 'pets' application.
"""
from django import forms
from pets.models import Pet

class PetRegistrationForm(forms.ModelForm):
    """
    Form definition which is used to to register and update pet.
    """
    class Meta:
        model = Pet
        fields = [
            'name',
            'location',
            'pet_type',
            'colour',
            'age',
            'size',
            'gender',
            'desexed',
            'collar',
            'microchipped',
            'microchipped_no',
            'missing_date',
            'status',
            'description',
            'pet_image',
        ]
        widgets = {
            'missing_date': forms.SelectDateWidget,
        }

    def __init__(self, user=None, *args, **kwargs):
        """
        Passing key word argurments to PetRegistrationForm
        """
        super(PetRegistrationForm, self).__init__(*args, **kwargs)
