from django.contrib import admin
from .models import Image, Property

# Register your models here.
admin.site.register(Property)
admin.site.register(Image)