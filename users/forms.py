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

CITY_CHOICE = []

all_city = CityData.objects.all()
i = 0

for city in all_city:
    CITY_CHOICE.append([i,city.city_name])
    i+=1

class ShopkeeperRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=15, required=False)
    city = forms.ChoiceField(choices = CITY_CHOICE)
    comment = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ShopkeeperRegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Email Address"
        self.fields['comment'].label = "Requirements/Expectations"

    class Meta:
        model = User
        fields = ['username','email','password1','password2','city','phone','comment']