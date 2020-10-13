from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from management.models import CityData
from django.contrib.auth.models import User
from users.models import UserProfile
from management.models import Address

# Create your views here.

def register(request):
    if request.method == 'POST':
        print(request.POST)
        pwd1 = request.POST.get('password1')
        pwd2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username,email=email,password=pwd1)
        user.save()
        user_profile = UserProfile.objects.create(user=user,mobile_number=phone,pwd=pwd1)
        user_profile.save()
        return redirect('/login')
    form = UserRegisterForm()
    context = {
        'form' : form,
        'cities' : CityData.objects.all(),
        'address' : Address.objects.all()[0]
    }
    return render(request,'users/register.html',context)