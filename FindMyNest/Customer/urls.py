from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [  
    path('',views.addproperty,name='addproperty'),
    path('payment/',views.payment,name='payment'),
    path('propertylist/',views.propertylist,name='propertylist'),
    path('property_single/<int:property_id>/',views.propertysingle,name='property_single'),
    path('update_property/<int:property_id>/', views.update_property, name='update_property'),
    path('add-to-wishlist/<int:property_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:property_id>/',views.remove_from_wishlist, name='remove_from_wishlist'),
]