from django.shortcuts import render,redirect
from .forms import UserRegisterForm, ShopkeeperRegisterForm, FreelancerRegisterForm
from management.models import CityData
from django.contrib.auth.models import User
from users.models import UserProfile, Shopkeeper, Freelancer
from management.models import Address

# Create your views here.

def register(request):
    if request.method == 'POST':
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

def register_shopkeepers(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        city = CityData.objects.get(id=int(request.POST.get('city')))
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        user_profile = Shopkeeper.objects.create(user=user, mobile_number=phone, pwd=password1, city=city, comment=comment)
        user.is_staff=True 
        user_profile.save()
        return redirect('/login')
    form = ShopkeeperRegisterForm()
    context = {
        'form' : form,
        'address' : Address.objects.all()[0]
    }
    return render(request,'users/register_shopkeeper.html', context)

def register_freelancer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        phone = request.POST.get('phone')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        
        user_profile = Freelancer.objects.create(user=user, mobile_number=phone, pwd=password1)
        user.is_staff=True 
        user_profile.save()
        return redirect('/login')
    form = FreelancerRegisterForm()
    context = {
        'form' : form,
        'address' : Address.objects.all()[0]
    }
    return render(request,'users/register_freelancer.html', context)