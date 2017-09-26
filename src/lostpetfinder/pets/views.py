# Class base view mixins that verified current authenticated user
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

from pets.forms import PetRegistrationForm, CommentForm
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
    def get_queryset(self, *args, **kwargs):
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


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('pets.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'pets/add_comment_to_post.html', {'form': form})
