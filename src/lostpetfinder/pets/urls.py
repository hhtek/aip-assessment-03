from django.conf.urls import url

from .views import (
    LostPetListView,
    LostPetCreateView,
    LostPetUpdateView,
    LostPetDetailView
)

urlpatterns = [
    url(r'^$', LostPetListView.as_view(), name='list'),
    url(r'^register/$', LostPetCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', LostPetUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/$', LostPetDetailView.as_view(), name='detail'),
]
