from django.contrib import admin
from .models import Image, Property,Feedback

# Register your models here.
admin.site.register(Property)
admin.site.register(Image)
admin.site.register(Feedback)
