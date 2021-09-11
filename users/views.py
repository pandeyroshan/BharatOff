from management.views import minilocations
from management.sms_delivery import send_username_password
from django.shortcuts import render,redirect
from .forms import UserRegisterForm, ShopkeeperRegisterForm, FreelancerRegisterForm, SalesRegistrationForm
from management.models import CityData
from django.contrib.auth.models import User
from users.models import UserProfile, Shopkeeper, Freelancer, SalesPerson, NotificationAlert, UserNotification
from management.models import Files, MiniLocation
from math import sin, cos, sqrt, atan2, radians
from management.models import Address

from management.mail_service import send_username_password_via_email
from .models import CustomerLogin, DeviceID, MonthlyWinner
from management.firebase import send_fcm_notification
import random
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test
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

def get_closest_minilocation(user_profile):
    min_distance = 100000005

    all_mini_locations = MiniLocation.objects.all()
    nearest_minilocation = None

    R = 6373.0

    for mini_location in all_mini_locations:
        lat1 = radians(float(user_profile.latitude))
        lon1 = radians(float(user_profile.longitude))
        lat2 = radians(mini_location.lat)
        lon2 = radians(mini_location.lon)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        if distance < min_distance:
            min_distance = distance
            nearest_minilocation = mini_location
    return nearest_minilocation

def create_notification_alert(request):
    if request.method == 'POST':
        offer = Files.objects.get(user=request.user)
        minilocations = offer.MiniLocation.all()
        notification_text = request.POST.get("notification_text")

        notification_alert = NotificationAlert.objects.create(sent_by=request.user, text=notification_text)
        notification_alert.minilocations.set(minilocations)
        notification_alert.save()

        # send the notification to all users 

        all_user_profiles = UserProfile.objects.all()

        print("All users: ", all_user_profiles)

        for user_profile in all_user_profiles:
            minilocation = get_closest_minilocation(user_profile)

            print("User: ", user_profile)
            print("location: ", minilocation)

            if minilocation in minilocations:
                # add the notification
                user_notification = UserNotification.objects.create(target_user = user_profile.user, notification_text = notification_text)
                user_notification.save()

                # get the Device-ids of the user and then send notification
                all_device = DeviceID.objects.all().filter(user=user_profile.user)

                print(all_device)

                for device in all_device:
                    send_fcm_notification(device.device_id, "Offer from BharatOff", notification_text)
    return redirect("/dashboard")

@user_passes_test(lambda user: user.is_superuser)
def rewards_homepage(request):

    if len(MonthlyWinner.objects.all()) >0:
        last_winners = MonthlyWinner.objects.all()[len(MonthlyWinner.objects.all())-1]
    else:
        last_winners = []

    all_time_winners = MonthlyWinner.objects.all()

    for i in range(len(all_time_winners)):
        all_time_winners[i].total_winners = len(all_time_winners[i].customers.all())
        all_time_winners[i].grand_total = len(all_time_winners[i].customers.all())*int(all_time_winners[i].prize)
        all_time_winners[i].all_winners = all_time_winners[i].customers.all()
    
    context = {
        "last_winners" : last_winners.customers.all(),
        "month_year" : last_winners.monthYear,
        "prize" : last_winners.prize,
        "all_time_winners" : all_time_winners,
    }
    return render(request, "users/winners_management.html", context=context)

@user_passes_test(lambda user: user.is_superuser)
def find_winners(request):
    total_customer = len(CustomerLogin.objects.all())

    total_winners = int(request.POST.get("total_winners"))
    prize_money = int(request.POST.get("prize_money"))

    random_customers_ids = random.sample(range(1, total_customer), total_winners)

    random_customers = []

    for random_customer_id in random_customers_ids:
        random_customers.append(CustomerLogin.objects.get(id=random_customer_id))

    today = datetime.today()

    months = {
        1 : "JAN", 2 : "FEB", 3 : "MAR", 
        4 : "APR", 5 : "MAY", 6 : "JUN", 
        7 : "JUL", 8 : "AUG", 9 : "SEP", 
        10 : "OCT", 11 : "NOV", 12: "DEC"
    }

    current_month_year = str(months.get(today.month))+"-"+str(today.year)

    monthly_winners = MonthlyWinner.objects.create(monthYear=current_month_year, prize=prize_money)
    monthly_winners.customers.set(random_customers)
    monthly_winners.save()

    return redirect("/rewards")