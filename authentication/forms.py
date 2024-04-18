# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class signUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, label='Full Name')
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes and IDs to form fields
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'id': 'username'})
        self.fields['email'].widget.attrs.update({'class': 'form-input', 'id': 'email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input', 'id': 'password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input', 'id': 'confirm_password'})

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phoneNum', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['phoneNum'].widget.attrs.update({'class': 'form-input', 'id': 'phoneNum'})
        self.fields['bio'].widget.attrs.update({'class': 'form-input', 'id': 'bio'})

class loginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes and IDs to form fields
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'id': 'username'})
        self.fields['password'].widget.attrs.update({'class': 'form-input', 'id': 'password'})

class editProfileForm(UserChangeForm):
    fullname = forms.CharField(max_length=100, required=True, label='Full Name')

    class Meta:
        model = User
        fields = ['username', 'email', 'fullname']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes and IDs to form fields
        self.fields['fullname'].widget.attrs.update({'class': 'form-input', 'id': 'fullname'})
        self.fields['email'].widget.attrs.update({'class': 'form-input', 'id': 'email'})
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'id': 'username'})
