from .models import Profile
from django import forms

class LoginForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control my-2','placeholder': 'Enter your Email','type': 'email','name': 'email'}))
    password =forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput(attrs={ 'class' : 'form-control my-3', 'placeholder':'Password','type':'password'}))
    class Meta:
        model=Profile
        fields=['email','password',]