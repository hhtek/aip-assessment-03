from django.conf.urls import url

from .views import (
    LostPetListView,
    OwnerPetListView,
    PetDetailView,
    PetCreateView,
    PetUpdateView,
    PetDeleteView,
    #PetCommentView,
)
app_name = 'pets'
urlpatterns = [
    url(r'^$', OwnerPetListView.as_view(), name='list'),
    # url(r'^$', LostPetListView.as_view(), name='list'),
    url(r'^register/$', PetCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PetUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PetDeleteView.as_view(), name='delete'),
    url(r'^(?P<slug>[\w-]+)/$', PetDetailView.as_view(), name='detail'),
    #url(r'^(?P<slug>[\w-]+)/comment/$', PetCommentView.as_view(), name='add_comment')
]
