from django import forms
from pets.models import Pet

class PetRegistrationForm(forms.ModelForm):
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
            'name': forms.TextInput(attrs={'class':'textinputclass'}), # widget connecting to CSS
            'missing_date': forms.SelectDateWidget,
        }

    # Passing key word argurments to PetRegistrationForm
    def __init__(self, user=None, *args, **kwargs):
        super(PetRegistrationForm, self).__init__(*args, **kwargs)