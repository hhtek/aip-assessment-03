"""lostpetfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from django.conf import settings
from django.conf.urls.static import static

from pets.views import (
    LostPetListView,
    ReunitedPetsListView,
)

urlpatterns = [
    url(r'^account/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^finder/pets/', include('pets.urls', namespace='pets')), # authenticated owner urls
    url(r'^pets/$', LostPetListView.as_view(), name='lost-pets'),
    url(r'^reunited-pets/$', ReunitedPetsListView.as_view(), name='reunited-pets'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^api/pets/', include('pets.api.urls', namespace='pets-api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
