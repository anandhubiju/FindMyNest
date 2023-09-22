from django.shortcuts import render, redirect
from requests import Request
from django.http import JsonResponse
from .models import Property,Image,PropertyView,Feedback
from .forms import PropertyForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Property, Image 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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


def submit_comment(request):
    if request.method == 'POST':
        # Check if the user is logged in and has a user profile
        if request.user.is_authenticated and hasattr(request.user, 'userprofile'):
            userprofile = request.user.userprofile
        else:
            userprofile = None

        first_name = request.POST['first_name']
        email = request.POST['email']
        message = request.POST['message']
        property_id = request.POST['property_id']

        # Create a new Feedback instance and save it to the database
        feedback = Feedback(
            userprofile=userprofile,  # Associate feedback with the user's profile
            property_id=property_id,
            first_name=first_name,
            email=email,
            message=message,
        )
        feedback.save()

        # Optionally, you can add a success message
        # messages.success(request, 'Your comment has been posted successfully.')

        # Redirect to the property_single page with the property_id
        return redirect('property_single', property_id=property_id)

    return render(request, 'property-single.html')
    


def propertylist(request):
    properties = Property.objects.all() 
    property_types = Property.objects.values_list('property_type', flat=True).distinct()
    
    return render(request,'propertylist.html', {'properties': properties})


def property_list_by_type(request, property_type):
   
    properties = Property.objects.filter(property_type=property_type)
    
    context = {
        'properties': properties,
        'selected_property_type': property_type,
        'property_types': property_type
    }
    
    return render(request, 'propertylist_by_type.html', context)


def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.user != property.user:
        pass
    property.delete()
    return redirect('propertylist') 

def edit_property(request, property_id):
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

            return redirect('propertylist') 
    else:
        form = PropertyForm(instance=property)

    return render(request, 'edit_property.html', {'form': form, 'property': property })




def propertysingle(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    feedbacks = Feedback.objects.filter(property=property).order_by('-comment_date')
    
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
    
    return render(request, 'property-single.html', {'property': property, 'images': images ,
    'features': features,'nearby_place': nearby_place,'excluded_property_types':excluded_property_types,'feedbacks': feedbacks,})

def like_feedback(request, feedback_id):
    # Check if the request is a POST request
    if request.method == 'POST':
        feedback = get_object_or_404(Feedback, id=feedback_id)

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check if the user has already liked the feedback
            if feedback.likes.filter(id=request.user.id).exists():
                # User has already liked, so unlike
                feedback.likes.remove(request.user)
                liked = False
            else:
                # User hasn't liked yet, so like
                feedback.likes.add(request.user)
                liked = True

            # Return a JSON response with the updated like status and count
            return JsonResponse({'liked': liked, 'likes_count': feedback.likes.count()})

    # Return a JsonResponse with an error message if the request is not valid
    return JsonResponse({'error': 'Invalid request'}, status=400)



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



