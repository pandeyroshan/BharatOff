from management.sms_delivery import send_username_password
from django.shortcuts import render,redirect
from .forms import UserRegisterForm, ShopkeeperRegisterForm, FreelancerRegisterForm, SalesRegistrationForm
from management.models import CityData
from django.contrib.auth.models import User
from users.models import UserProfile, Shopkeeper, Freelancer, SalesPerson   
from management.models import Address

from management.mail_service import send_username_password_via_email
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

def register_sales(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        phone = request.POST.get('phone')

        print(request.POST.get('city'))

        city = CityData.objects.get(id=int(request.POST.get('city')))

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        
        user_profile = SalesPerson.objects.create(user=user, mobile_number=phone, pwd=password1, city=city)
        user.is_staff=True 
        user_profile.save()
        return redirect('/login')
    form = SalesRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register_sales.html', context)

def update_password(request):
    user_id = request.GET.get('user_id')

    user = User.objects.get(id=int(user_id))
    try:
        salesperson = SalesPerson.objects.get(user= user)
        salesperson.pwd = request.GET.get('password')

        salesperson.save()
    except:
        shopkeeper = Shopkeeper.objects.get(user=user)
        shopkeeper.pwd = request.GET.get('password')

        shopkeeper.save()

    print('Password changed')

    return redirect('/login')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            profile = SalesPerson.objects.get(email=email)
        except:
            try:
                profile = Shopkeeper.objects.get(email=email)
            except:
                return redirect('/login')
        send_username_password_via_email(profile.user.username, profile.pwd, profile.email)
        return render(request,"users/password-sent-successful.html")
        pass
    return render(request,'users/forgot-password.html')