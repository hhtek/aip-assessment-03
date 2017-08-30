from django.conf.urls import url

from .views import (
    LostPetListView,
    PetListView,
    PetDetailView,
    PetCreateView,
    PetUpdateView,
    PetDeleteView,
)

urlpatterns = [
    url(r'^$', LostPetListView.as_view(), name='list'),
    url(r'^register/$', PetCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PetUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PetDeleteView.as_view(), name='delete'),
    url(r'^(?P<slug>[\w-]+)/$', PetDetailView.as_view(), name='detail'),
]
