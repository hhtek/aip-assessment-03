from django.conf.urls import url

from .views import (
    PetListAPIView,
    PetDetailAPIView,
    PetCreateAPIView,
    PetRetrieveUpdateAPIView,
    PetDeleteAPIView,
)

urlpatterns = [
    url(r'^$', PetListAPIView.as_view(), name='list'),
    url(r'^register/$', PetCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PetDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PetRetrieveUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PetDeleteAPIView.as_view(), name='delete'),
]
