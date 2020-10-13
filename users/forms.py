from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from management.models import CityData

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=15, required=False)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','phone']