# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import profile
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def login_page(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            if not User.objects.filter(username=username).exists():
                errors['username_error'] = "Username does not exist."
            else:
                errors['password_error'] = "Incorrect password. Please try again."
    return render(request, 'login.html', {'errors': errors})

def signup_page(request):
    errors = {}
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if User.objects.filter(username=uname).exists():
            errors['username_error'] = "Username already exists. Please choose a different username."
        if User.objects.filter(email=email).exists():
            errors['email_error'] = "An account with this email already exists. Please use a different email."
        if len(pass1) < 4:
            errors['password_error'] = "Password is too short. It must be at least 4 characters long."
        if pass1 != pass2:
            errors['confirm_password_error'] = "Your password and confirm password are not the same!"

        if not errors:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html', {'errors': errors})

@login_required
def profile_page(request):
    user_profile_instance, created = profile.objects.get_or_create(user=request.user)
    errors = {}  # Dictionary to store any validation errors

    if request.method == 'POST':
        img = request.FILES.get('img')
        bio = request.POST.get('bio')
        name = request.POST.get('name')
        birthday = request.POST.get('birthday')
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        location = request.POST.get('location')

        # Update fields if they have been provided
        if img:
            user_profile_instance.image = img
        if bio:
            user_profile_instance.bio = bio
        if name:
            user_profile_instance.name = name
        if birthday:
            user_profile_instance.birthday = birthday

        # Validate phone number
        if phone:
            if phone.isdigit() and len(phone) == 11:
                user_profile_instance.phone = phone
            else:
                errors['phone_error'] = "Invalid phone number. Please enter an 11-digit number."

        if gender:
            user_profile_instance.gender = gender    
        if location:
            user_profile_instance.location = location
        
        # Save only if there are no errors
        if not errors:
            user_profile_instance.save()
            return redirect('profile')  # Redirect after saving

    return render(request, 'profile.html', {'profile': user_profile_instance, 'user': request.user, 'errors': errors})

def Ulogout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def delete_profile(request):
    if request.method == 'POST':
        
        user = request.user
        user.delete()
        messages.success(request, "Your profile has been deleted successfully.")
        return redirect('signup')  

    return render(request, 'delete_profile.html')
