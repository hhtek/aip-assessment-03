# Class base view mixins that verified current authenticated user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q # filter using operators '&' or '|'
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.urlresolvers import reverse

# Django class base views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from pets.forms import PetRegistrationForm, CommentForm
from pets.models import Pet

# Display list of pets
class OwnerPetListView(ListView):
    """
    Get pets owned by the authenticated usser
    """
    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)

# Display list of pets
class LostPetListView(ListView):
    """
    Get list of lost pets
    """
    def get_queryset(self):
        return Pet.objects.filter(status__iexact='lost')

class ReunitedPetsListView(ListView):
    """
    Get list of reunited pets
    """
    def get_queryset(self):
        return Pet.objects.filter(status__iexact='found')

class PetDetailView(DetailView):
    """
    Get specific pet details
    """
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Pet.objects.filter(slug=slug)

class PetCreateView(LoginRequiredMixin, CreateView):
    """
    Pet registration
    """
    form_class = PetRegistrationForm
    template_name = 'pets/pet_form.html'
    login_url = 'login' # Redirect to login url if not authenticated

    # Get pets owned by the authenticated user
    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)

    # Form Validation
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user # current authenticated user
        return super(PetCreateView, self).form_valid(form)

    # Return the key word argurments for instantiating the form
    def get_form_kwargs(self):
        kwargs = super(PetCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # Get context data of the form
    def get_context_data(self, *args, **kwargs):
        context = super(PetCreateView, self).\
            get_context_data(*args, **kwargs)
        context['title'] = 'Pet Registration'
        return context

class PetUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update pet
    """
    form_class = PetRegistrationForm
    template_name = 'pets/pet_form.html'

    # Get pets owned by the authenticated user
    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)

    # Return the key word argurments for instantiating the form
    def get_form_kwargs(self):
        kwargs = super(PetUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # Get context data of the form
    def get_context_data(self, *args, **kwargs):
        context = super(PetUpdateView, self).\
            get_context_data(*args, **kwargs)
        context['title'] = 'Update Pet'
        return context

class PetDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete pet
    """
    success_url = reverse_lazy('pets:list') # Return to pets list

    # Get pets owned by the authenticated user
    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)

    # Get context data of the form
    def get_context_data(self, *args, **kwargs):
        context = super(PetDeleteView, self).\
            get_context_data(*args, **kwargs)
        context['title'] = 'Remove Pet Listing'
        return context
