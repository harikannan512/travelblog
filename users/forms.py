from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Bloguser


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Bloguser
        fields = ['username', 'email', 'password1', 'password2']


class UserProfile(forms.ModelForm):

    class Meta:
        model = Bloguser
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_pic', ]
