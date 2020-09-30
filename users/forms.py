from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from management.models import CityData

CITY_CHOICES = []

all_city = CityData.objects.all()

for city in all_city:
    new_city = []
    new_city.append(city.id)
    new_city.append(city.city_name)

    CITY_CHOICES.append(new_city)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    city = forms.ChoiceField(choices=CITY_CHOICES, help_text='Select nearest city from your location.')
    phone = forms.CharField(max_length=15, required=False)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','city','phone']