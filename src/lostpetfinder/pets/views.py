# from django.shortcuts import render
from django.db.models import Q # filter using operators '&' or '|'
# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
# from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from pets.models import LostPet

# Lost pet list view
class LostPetListView(ListView):
    #template_name = 'pets/lostpet_list.html'
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = LostPet.objects.filter(
                Q(name__iexact=slug) |
                Q(name__icontains=slug)
            )
        else:
            queryset = LostPet.objects.all()
            print(queryset)
        return queryset

# Lost pet detail view
class LostPetDetailView(DetailView):
    #template_name = 'pets/lostpet_list.html'
    #model = LostPet
    queryset = LostPet.objects.all()
