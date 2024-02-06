from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.contrib.auth import login as auth_login ,authenticate, logout
from django.shortcuts import render, redirect
from django.contrib  import messages,auth
from .models import CustomUser,UserProfile
from therapist.models import Therapist,TherapistDayOff,LeaveRequest
# from accounts.backends import EmailBackend
from django.contrib.auth import get_user_model
from .forms import CustomUserForm, UserProfileForm
from .forms import TherapistForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated
from .tokens import account_activation_token

########################################################################################################################

#User Reg and Login with acc activation , logout

########################################################################################################################

User = get_user_model()

def activate(request, uidb64, token):
    print("Reached the activate view")
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        print("Token is valid") 
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('index')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("email/account-activation.html", {
        ' '
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def userlogin(request):
    if request.user.is_authenticated:
        if request.user.role == CustomUser.CLIENT:
            return redirect('http://127.0.0.1:8000/')
        elif request.user.role == CustomUser.THERAPIST:
            return redirect(reverse('therapist'))
        elif request.user.role == CustomUser.ADMIN:
            return redirect(reverse('adminindex'))
        else:
            return redirect('http://127.0.0.1:8000/')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)  
        print(password)  

        if email and password:
            user = authenticate(request, email=email, password=password)
            print("Authenticated user:", user)  
            if user is not None:
                auth_login(request, user)
                print("User authenticated:", user.email, user.role)
                if request.user.role == CustomUser.CLIENT:
                    return redirect('http://127.0.0.1:8000/')
                elif request.user.role == CustomUser.THERAPIST:
                    return redirect(reverse('therapist'))
                elif request.user.role == CustomUser.ADMIN:
                    return redirect(reverse('adminindex'))
                else:
                    return redirect('http://127.0.0.1:8000/')

            else:
                error_message = "Invalid login credentials."
                return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = "Please fill out all fields."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

@user_not_authenticated
def register(request):
    if request.user.is_authenticated:
        if request.user.role == CustomUser.CLIENT:
            return redirect('http://127.0.0.1:8000/')
        elif request.user.role == CustomUser.THERAPIST:
            return redirect(reverse('therapist'))
        elif request.user.role == CustomUser.ADMIN:
            return redirect(reverse('adminindex'))
        else:
            return redirect('http://127.0.0.1:8000/')
    elif request.method == 'POST':
        name1 = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        password = request.POST.get('pass', None)
        confirm_password = request.POST.get('cpass', None)
        role = User.CLIENT

        if name1 and email and phone and password and role:
            if User.objects.filter(email=email).exists():
                error_message = "Email is already registered."
                return render(request, 'register2.html', {'error_message': error_message})
            
            elif password!=confirm_password:
                error_message = "Password's Don't Match, Enter correct Password"
                return render(request, 'register2.html', {'error_message': error_message})

            
            else:
                user = User(name=name1, email=email, phone=phone,role=role)
                user.set_password(password)  # Set the password securely
                user.is_active=False
                user.save()
                user_profile = UserProfile(user=user)
                user_profile.save()
                activateEmail(request, user, email)
                return redirect('login')  
            
    return render(request, 'register2.html')

def userLogout(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')




########################################################################################################################

#Add Therapist

########################################################################################################################

@login_required
def addTherapist(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)

        if user_form.is_valid():
            email = user_form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                msg = 'Email already exists. Please use a different email address.'
            else:
                user = user_form.save(commit=False)
                password = user_form.cleaned_data['password']

            # Send welcome email
                send_welcome_email(user.email, password, user.name)

                user.set_password(password)
                user.is_active = True

                user.role = CustomUser.THERAPIST  # Set the role to "Therapist"
                user.save()

            # Check if the user has the role=2 (Therapist)
                if user.role == CustomUser.THERAPIST:
                    therapist = Therapist(user=user)  # Create a Therapist instance
                    therapist.save()

                user_profile = UserProfile(user=user)
            
                user_profile.save()

                return redirect('adminindex')

    else:
        user_form = CustomUserForm()

    context = {
        'user_form': user_form
    }

    return render(request, 'add-therapist.html', context)



def send_welcome_email(email, password, therapist_name):

    login_url = 'http://127.0.0.1:8000/accounts/login/'  # Update with your actual login URL
    login_button = f'Click here to log in: {login_url}'


    subject = 'SoulCure - Therapist Registration'
    message = f"Hello {therapist_name},\n\n"
    message += f"Welcome to SoulCure, your platform for holistic wellness and healing. We are thrilled to have you on board as a part of our dedicated team of therapists.\n\n"
    message += f"Your registration is complete, and we're excited to have you join us. Here are your login credentials:\n\n"
    message += f"Email: {email}\nPassword: {password}\n\n"
    message += "Please take a moment to log in to your account using the provided credentials. Once you've logged in, we encourage you to reset your password to something more secure and memorable.\n\n"
    message += login_button
    message += "\n\nSoulCure is committed to providing a safe and supportive environment for both therapists and clients. Together, we can make a positive impact on the lives of those seeking healing and guidance.\n"
    message += "Thank you for joining the SoulCure community. We look forward to your contributions and the positive energy you'll bring to our platform.\n\n"
    message += "Warm regards,\nThe SoulCure Team\n\n"
    


    from_email='amalraj89903@gmail.com'
      # Replace with your actual email
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)


########################################################################################################################

#List Users

########################################################################################################################

def users_list(request):
    users = User.objects.all()
    return render(request, 'admin/view-users.html', {'users': users})



def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        # Handle form submission and update user details
        user.username = request.POST['username']
        user.email = request.POST['email']

        # Update user role based on the selected role option
        role = request.POST.get('role')
        if role == 'customer':
            user.is_staff = False
            user.is_superuser = False
        elif role == 'staff':
            user.is_staff = True
            user.is_superuser = False
        elif role == 'superuser':
            user.is_staff = True
            user.is_superuser = True

        user.save()
        return redirect('user_list')  # Redirect back to the user list page

    return render(request, 'admin/edituser.html', {'user': user})


########################################################################################################################

#View-therapies// admin main

########################################################################################################################
from therapist.models import Therapy
from therapist.forms import TherapyForm

from django.http import JsonResponse
from django.core import serializers
from .models import CustomUser
from client.models import Appointment

def view_therapies(request):
    therapies = Therapy.objects.all()
    context = {'therapies': therapies}
    return render(request, 'admin/view-therapies.html', context)


def susers(request):
    users = CustomUser.objects.all().exclude(role=4)
    return render(request, 'admin/users.html', {'users': users})


def view_appointments(request):
    appointments = Appointment.objects.all
    return render(request,'admin/view-appointments.html',{'appointments':appointments})


def updateuserStatus(request,update_id):
    updateUser=CustomUser.objects.get(id=update_id)
    if updateUser.is_active==True:
        updateUser.is_active=False
    else:
        updateUser.is_active=True
    updateUser.save()
    return redirect('susers')

def user_data(request):
    users = CustomUser.objects.all().exclude(role='Admin')
    data = serializers.serialize('json', users)
    return JsonResponse({'data': data}, safe=False)



def change_therapy_status(request, therapy_id):
    try:
        therapy = Therapy.objects.get(id=therapy_id)
        therapy.status = not therapy.status 
        therapy.save()
    except Therapy.DoesNotExist:
        pass

    return redirect('view-therapies') 

def update_therapy(request, therapy_id):
    therapy = get_object_or_404(Therapy, id=therapy_id) 

    if request.method == 'POST':
        form = TherapyForm(request.POST, instance=therapy)
        if form.is_valid():
            form.save()
            return redirect('view-therapies') 
    else:
        form = TherapyForm(instance=therapy)

    return render(request, 'admin/update_therapy.html', {'form': form, 'therapy': therapy})




########################################################################################################################

#View-leave Request// admin main

########################################################################################################################
@login_required
def view_leave_requests(request):
    # Check if the user is an admin
    if not request.user.role == 4:
        return redirect('/')  # Redirect to the home page or any other appropriate page

    # Query all pending holiday requests
    pending_requests = LeaveRequest.objects.filter(status='pending')

    # Render the template with the pending holiday requests data
    return render(request, 'admin/leave-request.html', {'pending_requests': pending_requests})

@login_required
def admin_approve_reject_leave(request, request_id):
    if request.method == 'POST':
        # Retrieve the holiday request object by its ID
        leave_request = get_object_or_404(LeaveRequest, pk=request_id)

        if request.POST['action'] == 'approve':
            # If the admin approves the holiday request, mark it as accepted
            leave_request.status = 'accepted'
            leave_request.save()

            # Get the associated lawyer profile
            therapist_profile = leave_request.therapist

            # Create a LawyerDayOff instance for the approved holiday
            TherapistDayOff.objects.create(therapist=therapist_profile, date=leave_request.date)
            print("Request ID:", request_id)


            messages.success(request, 'Leave request approved successfully.')

        elif request.POST['action'] == 'reject':
            # If the admin rejects the holiday request, mark it as rejected
            leave_request.status = 'rejected'
            leave_request.save()
            messages.success(request, 'Leave request rejected successfully.')

    # Redirect back to the admin dashboard or any other appropriate view
    return redirect('adminindex')  # Update this to the appropriate view name