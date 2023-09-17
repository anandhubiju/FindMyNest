from django.shortcuts import render, redirect
from requests import Request
from django.http import JsonResponse
from .models import Property,Image,PropertyView,Wishlist
from .forms import PropertyForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Property, Image 

@login_required
def addproperty(request):
    if request.method == 'POST':
        print(request.POST)
       
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            
            property_instance = form.save(commit=False)  # Don't save it immediately

           
            property_instance.user = request.user 

            
            selected_features = form.cleaned_data['features']
            features_str = ', '.join(selected_features)
            property_instance.features = features_str
            
            selected_nearby_place = form.cleaned_data['nearby_place']
            nearby_place_str = ', '.join(selected_nearby_place)
            property_instance.nearby_place = nearby_place_str

           
            property_instance.save()

           
            images = request.FILES.getlist('images')
            for image in images:
                
                Image.objects.create(property=property_instance, images=image)

           
            return redirect('/')
    else:
        form = PropertyForm()

    context = {
        'form': form,
    }
    return render(request, 'addproperty.html', context)



def payment(request):
    
    return render(request,'demopay.html')
    


def propertylist(request):
    properties = Property.objects.all() 
    return render(request,'propertylist.html', {'properties': properties})



def add_to_wishlist(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    user = request.user  # Assuming you have user authentication

    # Check if the property is not already in the wishlist
    if not Wishlist.objects.filter(property=property, user=user).exists():
        Wishlist.objects.create(property=property, user=user)

    return JsonResponse({"message": "Property added to wishlist"})

def remove_from_wishlist(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    user = request.user  # Assuming you have user authentication

    # Check if the property is in the wishlist
    wishlist_item = Wishlist.objects.filter(property=property, user=user).first()

    if wishlist_item:
        wishlist_item.delete()

    return JsonResponse({"message": "Property removed from wishlist"})



def propertysingle(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    if request.user != property.user:
        # Increment the view count
        property.view_count += 1
        property.save()

        # Record the user's view
        if request.user.is_authenticated:
            PropertyView.objects.get_or_create(property=property, user=request.user)
        
    images = Image.objects.filter(property=property)
    excluded_property_types = ['Commercial', 'Office', 'Garage']
    features = property.features.split(', ') if property.features else []
    nearby_place = property.nearby_place.split(', ') if property.nearby_place else []
    
    return render(request, 'property-single.html', {'property': property, 'images': images ,'features': features,'nearby_place': nearby_place,'excluded_property_types':excluded_property_types})



def update_property(request, property_id):
    
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        
        form = PropertyForm(request.POST, request.FILES, instance=property)
    
        if form.is_valid():
            updated_property = form.save(commit=False)
            
            
            selected_features = form.cleaned_data['features']
            features_str = ', '.join(selected_features)
            updated_property.features = features_str
            
            selected_nearby_place = form.cleaned_data['nearby_place']
            nearby_place_str = ', '.join(selected_nearby_place)
            updated_property.nearby_place = nearby_place_str

            images = request.FILES.getlist('images')
            if images:
                
                Image.objects.filter(property=updated_property).delete()
                
                for image in images:
                    property_image = Image(property=updated_property, images=image)
                    property_image.save()

            updated_property.save()

            return redirect('editprofile') 
    else:
        form = PropertyForm(instance=property)

    return render(request, 'update_property.html', {'form': form, 'property': property })



