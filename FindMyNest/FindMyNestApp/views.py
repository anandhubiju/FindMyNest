from django.shortcuts import render, redirect
from UserApp.models import CustomUser
from Customer.models import Property
from .models import Subscription
from django.urls import reverse
from django.views import View
from django.contrib.auth import get_user_model
from .forms import SubscriptionForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse

User = get_user_model()

def index(request):
    features = []
    subscription = Subscription.objects.all()
    
    
    if request.user.is_authenticated:
        # Check if the user is authenticated and logged in with Google
        if request.user.user_type == CustomUser.ADMIN:
            return redirect(reverse('admindashboard'))
        
        elif not request.user.phone_no:
            # If the user hasn't provided a phone number, redirect to profile completion
            return render(request, 'profile_completion.html', {'user': request.user})
    
    

    # Get the 5 most recently added properties based on the 'created_at' field
    recent_properties = Property.objects.order_by('-created_at')[:5]
    
    property_types = Property.objects.values_list('property_type', flat=True).distinct()
    

    return render(request, 'index.html', {'user': request.user, 'recent_properties': recent_properties , 'subscription':subscription,'property_types': property_types,})

def about(request):
    property_types = Property.objects.values_list('property_type', flat=True).distinct()
    return render(request,'about.html',{'property_types': property_types})


def add_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            sub_type = form.cleaned_data['sub_type']
            price = form.cleaned_data['price']
            validity = form.cleaned_data['validity']
            features_list = form.cleaned_data['features'].split(',')
            features_csv = ','.join(features_list)
            

            if Subscription.objects.filter(
                sub_type=sub_type,
                price=price,
                validity=validity,
                features=features_csv
            ).exists():
                
                form.add_error(None, "A subscription with the same data already exists.")
            else:
               
                subscription = form.save(commit=False)
                subscription.features = features_csv
                subscription.save()
                return redirect('admindashboard')
    else:
        form = SubscriptionForm()
    
    return render(request, 'add_subscription.html', {'form': form})
 # Replace 'search.html' with your template


@login_required
def search_property(request):
    query = request.GET.get('query')
    print("Query:", query)

   
    if query:
        properties = Property.objects.filter(
            Q(property_type__icontains=query) | Q(Town__icontains=query) | Q(state__icontains=query) 
        )
    else:
       
        properties = []
    property_data = []
    
    for property in properties:
        
        property_dict = {
            'id': property.pk,
            'thumbnail': property.thumbnail.url,
            'address':  property.address,
            'property_type':  property.property_type,
            'bathrooms':  property.bathrooms,
            'bedrooms':  property.bedrooms,
            'price':  property.price,
            'area':  property.area,
        }
        property_data.append(property_dict)

    return JsonResponse({'property': property_data})