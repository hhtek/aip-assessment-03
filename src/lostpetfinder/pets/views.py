from django.shortcuts import render
from django.db.models import Q # filter using operators '&' or '|'
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView
    )

from .forms import LostPetRegistrationForm
from .models import LostPet

# Lost pet list view: display list of pets
class LostPetListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = LostPet.objects.filter(
                Q(name__iexact=slug) |
                Q(name__icontains=slug)
            )
        else:
            queryset = LostPet.objects.all()
        return queryset

# Lost pet detail view: display specific pet details
class LostPetDetailView(DetailView):
    model = LostPet

# Lost pet create view: used for pet registration 
class LostPetCreateView(CreateView):
    form_class = LostPetRegistrationForm
    template_name = 'pets/form.html'
    success_url = '/pets/'
