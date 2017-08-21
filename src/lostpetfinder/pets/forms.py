from django.forms import ModelForm, Textarea, SelectDateWidget

from .models import LostPet

class LostPetRegistrationForm(ModelForm):
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
        widgets = {
            'missing_date': SelectDateWidget,
        }
