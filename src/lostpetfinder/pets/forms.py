from django.forms import ModelForm, Textarea, SelectDateWidget

from .models import Pet

class PetRegistrationForm(ModelForm):
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
            'description'
        ]
        widgets = {
            'missing_date': SelectDateWidget,
        }

    # Passing key word argurments to PetRegistrationForm
    def __init__(self, user=None, *args, **kwargs):
        super(PetRegistrationForm, self).__init__(*args, **kwargs)
