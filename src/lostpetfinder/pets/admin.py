from django.contrib import admin
from .models import Pet

# Model registration
admin.site.register(Pet) # register Pet application to admin.site
