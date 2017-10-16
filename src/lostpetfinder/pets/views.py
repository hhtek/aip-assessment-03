"""
Django views classes which are used to handle business domain of
the pets application.
"""
# Class base view mixins that verify current authenticated user
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q # filter using operators '&' or '|'
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.urlresolvers import reverse, resolve

# Django generic class base views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from pets.forms import PetRegistrationForm
from pets.models import Pet

class PetListView(ListView):
    """
    Get list of pets:
        GET /finder/pets: get pets owned by authenticated user.
        GET /pets: get pets with lost status.
        GET /reunited-pets: get pets with found status.
        GET pets/search/?q=[query]:
            search pets with status, pet type, pet name, and location
    """
    context_object_name = 'pets' # change default object_list to pets
    paginate_by = 6 # display 6 pets per page

    def get_queryset(self, *args, **kwargs):
        """
        Return a list of pets based on search filter
        """
        # get requested URL namespace
        url_name = resolve(self.request.path).url_name

        if(url_name == 'list'): # GET /finder/pets/ (refer to pets.urls)
            return Pet.objects.filter(owner=self.request.user)

        if(url_name == 'lost-pets'): # GET /pets
            return Pet.objects.filter(status__iexact='lost')

        if(url_name == 'reunited-pets'): # GET /reunited-pets
            return Pet.objects.filter(status__iexact='found')

        if(url_name == 'search-pets'): # GET /pets/search/?q=[query]
            # Exclude pet with registered status from search query
            # hide pet with 'Registered' status from public view
            queryset = Pet.objects.exclude(status__iexact='registered')

            query = self.request.GET.get('q')
            if query:
                search_list = queryset.filter(
                    Q(status__iexact=query)|
                    Q(name__icontains=query)|
                    Q(location__icontains=query)|
                    Q(pet_type__iexact=query)
                ).distinct()
                return search_list
            return queryset

    def get_context_data(self, *args, **kwargs):
        """
        Get context data of page
        """
        context = super(PetListView, self).\
            get_context_data(*args, **kwargs)

        # get requested URL namespace
        url_name = resolve(self.request.path).url_name
        title = 'My Pets' # default title to be 'My Pets'

        if(url_name == 'lost-pets'):
            title = 'Lost Pets'

        if(url_name == 'reunited-pets'):
            title = 'Found Pets'

        context['title'] = title
        return context

class PetDetailView(DetailView):
    """
    Get specific pet details
        GET /finder/pets/slug/
    """
    def get_queryset(self):
        """
        Get specific pet based on pet's slug
        """
        slug = self.kwargs.get('slug')
        return Pet.objects.filter(slug=slug)

    def get_context_data(self, *args, **kwargs):
        """
        Get context data for rendering 'pets/pet_detail.html'
        """
        slug = self.kwargs.get('slug')
        pet = Pet.objects.get(slug=slug)
        petLatLng = pet.get_geolocation_data() # get pet's geolocation from API

        context = super(PetDetailView, self).\
            get_context_data(*args, **kwargs)

        context['title'] = pet.name
        context['lat'] = petLatLng['lat'] # pet's latitude
        context['lng'] = petLatLng['lng'] # pet's longitude

        # Define bootstrap CSS classes for rendering
        # 'pets/pet_detail_data.html'base on pet's status
        if(pet.status.lower() == 'lost'):
            context['bt_badge_css'] = "badge-danger"
        if(pet.status.lower() == 'found'):
            context['bt_badge_css'] = "badge-primary"
        if(pet.status.lower() == 'registered'):
            context['bt_badge_css'] = "badge-warning"
        return context

class PetCreateView(LoginRequiredMixin, CreateView):
    """
    Pet registration
    POST /pets/register
    """
    form_class = PetRegistrationForm
    template_name = 'pets/pet_form.html'
    login_url = 'login' # Redirect to login url if not authenticated

    def get_queryset(self):
        """
        Get pets owned by the current authenticated user
        """
        return Pet.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        """
        Form Validation
        """
        instance = form.save(commit=False)
        instance.owner = self.request.user # current authenticated user
        return super(PetCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        """
        Return the key word argurments for instantiating the form
        """
        kwargs = super(PetCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        """
        Get context data for rendering a HTML page
        """
        context = super(PetCreateView, self).\
            get_context_data(*args, **kwargs)
        context['title'] = 'Pet Registration'
        return context

class PetUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update specific pet
        POST /finder/pets/{slug-field}/edit/
    """
    form_class = PetRegistrationForm
    template_name = 'pets/pet_form.html'

    def get_queryset(self):
        """
        Get pets owned by the authenticated user
        """
        return Pet.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        """
        Return the key word argurments for instantiating the form
        """
        kwargs = super(PetUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        """
        Get context data for rendering a HTML page
        """
        slug = self.kwargs.get('slug')
        pet = Pet.objects.get(slug=slug)
        context = super(PetUpdateView, self).\
            get_context_data(*args, **kwargs)
        context['title'] = f'Edit {pet.pet_type}: {pet.name.upper()}'
        return context

class PetDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete specific pet
        POST /finder/pets/pets/delete
    """
    success_url = reverse_lazy('pets:list') # Return to pets list

    def get_queryset(self):
        """
        Get pets owned by the authenticated user
        """
        return Pet.objects.filter(owner=self.request.user)

    def get_context_data(self, *args, **kwargs):
        """
        Get context data for rendering HTML page
        """
        context = super(PetDeleteView, self).\
            get_context_data(*args, **kwargs)
        pet = Pet.objects.get(slug=self.kwargs.get('slug'))
        context['title'] = pet.name
        return context
