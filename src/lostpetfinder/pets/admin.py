from django.contrib import admin
from .models import Pet, Comment

# Models registration
admin.site.register(Pet)
admin.site.register(Comment)
