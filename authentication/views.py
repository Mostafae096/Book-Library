from django.shortcuts import render, redirect
from .forms import signUpForm, loginForm, editProfileForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.

def userlogin(request):
    if request.method == 'POST':
        form = loginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or home
                return redirect('Home')
            else:
                # Handle invalid login
                form.add_error(None, 'Invalid login credentials')
    else:
        form = loginForm()

    return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            # Save the user created by the signUpForm
            user = form.save()

            # Save the profile with the correct user
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Redirect to the login page
            return redirect(reverse('login'))
        else:
            print("Form validation failed.")
            print(form.errors)
            print(profile_form.errors)
    else:
        form = signUpForm()
        profile_form = UserProfileForm()

    return render(request, "account/register.html", {'form': form, 'profile_form': profile_form})



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = editProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('Home')  # Check that 'Home' is the correct name defined in your URLs
    else:
        form = editProfileForm(instance=request.user)

    return render(request, 'account/edit.html', {'form': form})

