from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.fields import CharField

class loginForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']

class createUserForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username','email','password1','password2']
