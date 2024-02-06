from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'), 
    path('dashboard/',views.dashboard,name='dashboard'), 
    path('agentlist/',views.agentlist,name='agentlist'),
    path('agentsingle/<int:agentProfile_id>/',views.agentsingle,name='agentsingle'), 
    path('add_subscription/',views.add_subscription,name='add_subscription'),
    path('add_agent/',views.add_agent,name='add_agent'),
    path('search_property/',views.search_property,name='search_property'), 
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('payment/<int:sub_id>/',views.payment,name='payment'),
]