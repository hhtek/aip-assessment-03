from django.shortcuts import render
from django.db.models import Q # filter using operators '&' or '|'
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView
    )

from .forms import LostPetRegistrationForm
from .models import LostPet

# Display list of lost pets
class LostPetListView(ListView):
    queryset = LostPet.objects.filter(status__iexact='lost')

# Display list of reunited-pets
class ReunitedPetsListView(ListView):
    queryset = LostPet.objects.filter(status__iexact='found')

# Display specific pet details
class LostPetDetailView(DetailView):
    model = LostPet

# Lost pet registration form
class LostPetCreateView(CreateView):
    template_name = 'pets/form.html'
    form_class = LostPetRegistrationForm
    success_url = '/pets/'

# Lost pet update form
class LostPetUpdateView(UpdateView):
    model = LostPet
    template_name = 'pets/form.html'
    form_class = LostPetRegistrationForm
    success_url = '/pets/'
