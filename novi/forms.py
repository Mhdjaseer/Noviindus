from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=50,help_text='Enter a valid address ')

    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]