from django import forms

from .models import LostPet

class LostPetRegistrationForm(forms.ModelForm):
    class Meta:
        model = LostPet
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
            'description'
        ]
