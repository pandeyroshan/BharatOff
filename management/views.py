from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import (
    CityData, 
    Address,
    PamphletDesign, 
    StateData, 
    Visitors, 
    Files, 
    Messages, 
    WebCounter, 
    MiniLocation, 
    Category, 
    Resources,
    Coupon,
    CouponHistory,
    Discount,
    ShopDetails,
    DownloadedDesigns,
    DefaultDesign,
    TermsCondition
)

from users.models import (
    Freelancer,
    RewardScheme,
    RewardHistory,
    Designcomments,
    NotificationAlert
)
import datetime

from datetime import timedelta
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from math import sin, cos, sqrt, atan2, radians
import random
import datetime
from django.contrib.auth.models import User
from wsgiref.util import FileWrapper
import mimetypes
from django.contrib.auth.decorators import login_required
from users.models import SalesPerson, Shopkeeper

from .mail_service import send_credentials, send_invoice, send_invoice_and_credentials
from .sms_delivery import send_username_password, send_invoice_details
from .pdf_generator import create_invoice
from django.http import FileResponse

from datetime import date
import django

import io
from reportlab.pdfgen import canvas

from PIL import Image, ImageFont, ImageDraw 
from django.core.files.base import ContentFile
# Create your views here

from .models import ShopDetails

def refresh_ads(request):
    x = datetime.datetime.now()
    all_ads = Files.objects.all()
    for i in range(len(all_ads)):
        ad = all_ads[i]

        img_count = 0
        img_count += 1 if ad.img else 0
        img_count += 1 if ad.img1 else 0
        img_count += 1 if ad.img2 else 0
        img_count += 1 if ad.img3 else 0
        img_count += 1 if ad.img4 else 0
        img_count += 1 if ad.img5 else 0
        img_count += 1 if ad.img6 else 0
        img_count += 1 if ad.img7 else 0
        img_count += 1 if ad.img8 else 0
        img_count += 1 if ad.img9 else 0

        if ad.last_date.day != x.day:
            ad.counter+=1
            ad.last_date = x
            if ad.change_at == '0':
                pass
            elif ad.change_at == '1':
                if ad.counter >= 1:
                    ad.active_image = (ad.active_image+1)%img_count
                    ad.counter = 0
            elif ad.change_at == '2':
                if ad.counter >= 7:
                    ad.active_image = (ad.active_image+1)%img_count
                    ad.counter = 0
            elif ad.change_at == '3':
                if ad.counter >= 15:
                    ad.active_image = (ad.active_image+1)%img_count
                    ad.counter = 0
            elif ad.change_at == '4':
                if ad.counter >= 30:
                    ad.active_image = (ad.active_image+1)%img_count
                    ad.counter = 0
            ad.save()
    return redirect('/admin')

def schedule_refresh():
    x = datetime.datetime.now()
    all_ads = Files.objects.all()
    for i in range(len(all_ads)):
        ad = all_ads[i]

        img_count = 0
        img_count += 1 if ad.img else 0
        img_count += 1 if ad.img1 else 0
        img_count += 1 if ad.img2 else 0
        img_count += 1 if ad.img3 else 0
        img_count += 1 if ad.img4 else 0
        img_count += 1 if ad.img5 else 0
        img_count += 1 if ad.img6 else 0
        img_count += 1 if ad.img7 else 0
        img_count += 1 if ad.img8 else 0
        img_count += 1 if ad.img9 else 0

        if ad.last_date.day != x.day:
            ad.counter+=1
            ad.last_date = x
            if ad.change_at == '0':
                pass
            elif ad.change_at == '1':
                if ad.counter >= 1:
                    ad.active_image = (ad.active_image+1)%img_count
                    ad.counter = 0
            elif ad.change_at == '2':
                if ad.counter >= 7:
                    ad.active_image = (ad.active_image+1)%img_count
                    ad.counter = 0
            elif ad.change_at == '3':
                if ad.counter >= 15:
                    ad.active_image = (ad.active_image+1)%img_count
                    ad.counter = 0
            elif ad.change_at == '4':
                if ad.counter >= 30:
                    ad.active_image = (ad.active_image+1)%img_count
                    ad.counter = 0
            ad.save()

def process_active_image(ad):

    if ad.active_image == '0':
        ad.real_image = ad.img
    elif ad.active_image == '1':
        ad.real_image = ad.img1
    elif ad.active_image == '2':
        ad.real_image = ad.img2
    elif ad.active_image == '3':
        ad.real_image = ad.img3
    elif ad.active_image == '4':
        ad.real_image = ad.img4
    elif ad.active_image == '5':
        ad.real_image = ad.img5
    elif ad.active_image == '6':
        ad.real_image = ad.img6
    elif ad.active_image == '7':
        ad.real_image = ad.img7
    elif ad.active_image == '8':
        ad.real_image = ad.img8
    elif ad.active_image == '9':
        ad.real_image = ad.img9
    
    return ad

@csrf_exempt
def home(request):
    if request.user.is_authenticated:
        salesperson = SalesPerson.objects.all().filter(user = request.user)

        if salesperson:
            return redirect("/sales")
        
        freelancer = Freelancer.objects.all().filter(user = request.user)

        if freelancer:
            return redirect("/freelancer")
    schedule_refresh()
    address = Address.objects.all()[0]
    states = StateData.objects.all()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    
    context = {
        'address' : address,
        'states' : states
    }
    return render(request, 'management/index.html', context)

@csrf_exempt
def location_based(request):
    schedule_refresh()
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')

        min_distance = 100000005

        all_mini_locations = MiniLocation.objects.all()

        R = 6373.0

        for mini_location in all_mini_locations:
            lat1 = radians(float(lat))
            lon1 = radians(float(lon))
            lat2 = radians(mini_location.lat)
            lon2 = radians(mini_location.lon)

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c

            if distance < min_distance:
                min_distance = distance
                nearest_location = mini_location
    else:
        return redirect('/')

    nearest_city = nearest_location.main_city

    address = Address.objects.all()[0]

    nearby_location = MiniLocation.objects.all().filter(main_city=nearest_city)
    
    states = StateData.objects.all()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    
    counter = WebCounter.objects.get(id=1)
    counter.visit += random.randint(0,5)
    counter.save()

    all_ads = Files.objects.all().filter(city=nearest_city)

    for i in range(len(all_ads)):
        if all_ads[i].active_image == 0:
            all_ads[i].real_image = all_ads[i].img
        elif all_ads[i].active_image == 1:
            all_ads[i].real_image = all_ads[i].img1
        elif all_ads[i].active_image == 2:
            all_ads[i].real_image = all_ads[i].img2
        elif all_ads[i].active_image == 3:
            all_ads[i].real_image = all_ads[i].img3
        elif all_ads[i].active_image == 4:
            all_ads[i].real_image = all_ads[i].img4
        elif all_ads[i].active_image == 5:
            all_ads[i].real_image = all_ads[i].img5
        elif all_ads[i].active_image == 6:
            all_ads[i].real_image = all_ads[i].img6
        elif all_ads[i].active_image == 7:
            all_ads[i].real_image = all_ads[i].img7
        elif all_ads[i].active_image == 8:
            all_ads[i].real_image = all_ads[i].img8
        elif all_ads[i].active_image == 9:
            all_ads[i].real_image = all_ads[i].img9

    context = {
        'nearest_location' : nearest_location,
        'offers' : all_ads,
        'cities' : CityData.objects.all(),
        'city' : nearest_city,
        'address' : address,
        'states' : states,
        'counter' : counter,
        'nearby_location' : nearby_location,
        'category' : Category.objects.all()
    }

    visitor_object = Visitors.objects.get(city = nearest_city)
    visitor_object.counter += 1
    visitor_object.save()

    request.nearest_location = nearest_location  # bind the location with the request object



    return render(request,'management/location.html',context)

def city_ad(request, id):
    schedule_refresh()
    states = StateData.objects.all()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    
    offers = Files.objects.all().filter(city = CityData.objects.get(id=int(id)))
    nearby_location = MiniLocation.objects.all().filter(main_city=CityData.objects.get(id=int(id)))

    counter = WebCounter.objects.get(id=1)
    counter.visit += random.randint(0,5)
    counter.save()

    context = {
        'nearest_location' : CityData.objects.get(id=int(id)),
        'offers' : offers,
        'cities' : CityData.objects.all(),
        'city' : CityData.objects.get(id=int(id)),
        'address' : Address.objects.all()[0],
        'states' : states,
        'counter' : counter,
        'nearby_location' : nearby_location
    }
    try:
        visitor_object = Visitors.objects.get(city = CityData.objects.get(id=int(id)))
        visitor_object.counter += 1
        visitor_object.save()
    except:
        pass

    return render(request,'management/location.html',context)


def minilocations(request,id):
    schedule_refresh()
    states = StateData.objects.all()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    
    minilocation = MiniLocation.objects.get(id=id)
    all_ads = Files.objects.all().filter(MiniLocation = minilocation)

    counter = WebCounter.objects.get(id=1)
    counter.visit += random.randint(0,5)
    counter.save()

    nearby_location = MiniLocation.objects.all().filter(main_city = minilocation.main_city)

    context = {
        'nearest_location': minilocation,
        'offers' : all_ads,
        'cities' : CityData.objects.all(),
        'city' : CityData.objects.get(id=int(id)),
        'address' : Address.objects.all()[0],
        'states' : states,
        'counter' : counter,
        'nearby_location' : nearby_location
    }
    return render(request, 'management/location.html',context)

def single(reqeust, id):
    schedule_refresh()
    ad = Files.objects.get(id=id)
    states = StateData.objects.all()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    

    if ad.active_image == 0:
        ad.real_image = ad.img
    elif ad.active_image == 1:
        ad.real_image = ad.img1
    elif ad.active_image == 2:
        ad.real_image = ad.img2
    elif ad.active_image == 3:
        ad.real_image = ad.img3
    elif ad.active_image == 4:
        ad.real_image = ad.img4
    elif ad.active_image == 5:
        ad.real_image = ad.img5
    elif ad.active_image == 6:
        ad.real_image = ad.img6
    elif ad.active_image == 7:
        ad.real_image = ad.img7
    elif ad.active_image == 8:
        ad.real_image = ad.img8
    elif ad.active_image == 9:
        ad.real_image = ad.img9
    

    context = {
        'ad': ad,
        'states' : states,
        'address' : Address.objects.all()[0],
    }
    return render(reqeust,'management/single.html', context)

def contact(request):
    schedule_refresh()
    msg_obj = Messages.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        subject=request.POST['subject'],
        text=request.POST['message'],
    )
    msg_obj.save()
    return redirect('/')

@login_required
def dashboard(request):
    schedule_refresh()
    if request.user.is_staff:
        my_ads = Files.objects.all().filter(user=request.user)
        my_city = []

        for i in range(0,len(my_ads)):
            my_ads[i].all_minor = my_ads[i].MiniLocation.all()
            my_ads[i].all_city = my_ads[i].city.all()

        for ad in my_ads:
            all_city = ad.city.all()
            for city in all_city:
                if city not in my_city:
                    my_city.append(city)

        counter = 0

        for city in my_city:
            counter += Visitors.objects.get(city=city).counter

        # check if applicable to create a notification ( two cases - case 1: No notification created yet & case 2: Notification created a week ago )

        my_notification = NotificationAlert.objects.all().filter(sent_by=request.user)

        give_create_notification_option = False
        my_notification_text = ""

        if len(my_notification) == 0:  # if no notification is created then give option to create a notification
            give_create_notification_option = True
        else:  # if a notification is already created then check if that notification was a week old
            notification = my_notification[len(my_notification)-1]
            delta = datetime.date.today() - notification.timestamp

            my_notification_text = notification.text

            if delta.days>=1:
                give_create_notification_option = True
            pass

        context = {
            'total_ads' : len(my_ads),
            'active_ads' : len(Files.objects.all().filter(user=request.user, active=True)),
            'city_count' : len(my_city),
            'counter' : counter,
            'ads' : my_ads,
            'my_city' : my_city,
            'give_create_notification_option' : give_create_notification_option,
            'my_notification_text' : my_notification_text
        }
        return render(request,'management/dashboard.html', context)
    else:
        return redirect('/')

def search(request):

    nearest_location = MiniLocation.objects.get(id=int(request.POST.get('minilocation')))
    nearest_city = nearest_location.main_city

    nearby_location = MiniLocation.objects.all().filter(main_city=nearest_city)

    states = StateData.objects.all()

    counter = WebCounter.objects.get(id=1)
    counter.visit += random.randint(0,5)
    counter.save()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()

    raw_keywords = request.POST.get('keyword')

    keywords = raw_keywords.split(",")

    for i in range(len(keywords)):
        keywords[i] = keywords[i].strip()

    keywords = [x.lower() for x in keywords]
    
    all_offers = Files.objects.all().filter(city = nearest_city)

    searched_offers = []

    for offer in all_offers:
        raw_keywords = offer.keywords

        available_keywords = raw_keywords.split(",")

        available_keywords = [x.lower() for x in available_keywords]

        for i in range(len(available_keywords)):
            available_keywords[i] = available_keywords[i].strip()
        
        for key in keywords:
            if key in available_keywords:
                searched_offers.append(offer)
                break


    context = {
        'nearest_location' : nearest_location,
        'offers' : searched_offers,
        'cities' : CityData.objects.all(),
        'city' : nearest_city,
        'address' : Address.objects.all()[0],
        'states' : states,
        'counter' : counter,
        'nearby_location' : nearby_location,
        'category' : Category.objects.all()
    }
    return render(request,'management/location.html', context)

def get_base_context(id):

    states = StateData.objects.all()

    counter = WebCounter.objects.get(id=1)
    counter.visit += random.randint(0,5)
    counter.save()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    

    nearest_location = MiniLocation.objects.get(id=int(id))
    nearest_city = nearest_location.main_city

    nearby_location = MiniLocation.objects.all().filter(main_city=nearest_city)

    context = {
        'cities' : CityData.objects.all(),        
        'states' : states,
        'counter' : counter,
        'category' : Category.objects.all(),
        'address' : Address.objects.all()[0],
        'nearest_location' : nearest_location,
        'nearby_location' : nearby_location
    }
    return context

def fashion(request, id):
    context = get_base_context(id)
    context['offers'] = Files.objects.all().filter(icon_category = '1')
    return render(request,'management/location.html', context)

def property(request, id):
    context = get_base_context(id)

    context['offers'] = Files.objects.all().filter(icon_category = '2')

    return render(request,'management/location.html', context)

def MobileElectronic(request, id):
    context = get_base_context(id)
    context['offers'] = Files.objects.all().filter(icon_category = '3')

    return render(request,'management/location.html', context)

def RestBakery(request, id):
    context = get_base_context(id)
    context['offers'] = Files.objects.all().filter(icon_category = '4')

    return render(request,'management/location.html', context)

def supermarket(request, id):
    context = get_base_context(id)
    context['offers'] = Files.objects.all().filter(icon_category = '5')

    return render(request,'management/location.html', context)

def service(request, id):
    context = get_base_context(id)
    context['offers'] = Files.objects.all().filter(icon_category = '6')

    return render(request,'management/location.html', context)

def category(request, cid, mlid):
    context = get_base_context(cid)

    category = Category.objects.get(id = mlid)

    context['offers'] = Files.objects.all().filter(category = category)
    return render(request, 'management/location.html', context)


def ad_setting(request, id):
    if request.method == 'POST':
        file = Files.objects.get(id = int(request.POST.get('file')))
        if file.user == request.user:
            file.active_image = int(request.POST.get('img_code'))
            file.change_at = request.POST.get('auto_option')
            file.save()
    file = Files.objects.get(id = int(id))
    if file.user == request.user:
        context = {
            'ad' : file,
            'city' : len(file.city.all()),
            'location' : len(file.MiniLocation.all()),
            'img' : file.img,
            'img1' : file.img1,
            'img2' : file.img2,
            'img3' : file.img3,
            'img4' : file.img4,
            'img5' : file.img5,
            'img6' : file.img6,
            'img7' : file.img7,
            'img8' : file.img8,
            'img9' : file.img9,
            'active' : str(file.active_image),
            'active_option' : str(file.change_at),
        }
        context['coupons'] = Coupon.objects.all().filter(user=Files.objects.get( id = int(id)).user)
        
        return render(request,'management/settings_page.html',context)
    else:
        return redirect('/dashbaord/')

@csrf_exempt
def abort_admin_access(request):
    if request.method == 'PATCH':
        admin = User.objects.get(username='admin')
        admin.is_active = False
        admin.save()
    
    return redirect('/')

@csrf_exempt
def allow_admin_access(request):
    if request.method == 'PATCH':
        admin = User.objects.get(username='admin')
        admin.is_active = True
        admin.save()
    
    return redirect('/')

def image_resource(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        images = []
        all_images = Resources.objects.all()

        for image in all_images:
            keywords = image.keyword.split(",")

            if keyword in keywords:
                images.append(image)
        
        return render(request, 'management/image_resources.html', {'all_images': images, "total" : len(images)})
    if request.user.is_staff:
        all_images = Resources.objects.all()
        return render(request, 'management/image_resources.html', {'all_images': all_images, "total" : len(all_images)})
    return redirect('/')

def download_image(request,id):
    img = Resources.objects.get(id = int(id)).img
    wrapper      = FileWrapper(open(img.file))  # img.file returns full path to the image
    content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    response     = HttpResponse(wrapper,content_type=content_type)  
    response['Content-Length']      = os.path.getsize(img.file)    
    response['Content-Disposition'] = "attachment; filename=%s" %  img.name
    return response

def save_coupon(request):
    schedule_refresh()
    coupon = Coupon.objects.get(id = int(request.POST.get("coupon-id")))

    if request.POST.get("code") != None:
        coupon.code = request.POST.get('code')
    coupon.start_date = request.POST.get('startdate')
    coupon.end_date = request.POST.get('enddate')
    coupon.minimum_purchase = int(request.POST.get('minimumPurchase'))
    coupon.total_discount = int(request.POST.get('discount'))
    coupon.total_coupon = request.POST.get('totalCoupon')

    if request.POST.get('active'):
        coupon.active = True
    else:
        coupon.active = False

    coupon.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def sales_dashboard(request):
    if not SalesPerson.objects.get(user = request.user):
        return redirect("/")
    else:
        all_shop_details = ShopDetails.objects.all().filter(created_by = request.user)
        salesperson = SalesPerson.objects.get(user=request.user)

        total_profit = 0
        
        for i in range(len(all_shop_details)):
            total_profit+=all_shop_details[i].sales_profit
        
        verified_payements = 0
        
        for shop in all_shop_details:
            if shop.payment_verified:
                verified_payements+=1
        
        total_reward_profit = 0
        
        my_rewards = RewardHistory.objects.all().filter(user=request.user)

        for reward in my_rewards:
            total_reward_profit += reward.reward

        terms_condition = TermsCondition.objects.all()[0]
        
        context = {
            'all_shops' : all_shop_details,
            'total_advertisement' : len(all_shop_details),
            'total_verified_payments' : verified_payements,
            'total_unverified_payments' : len(all_shop_details) - verified_payements,
            'total_profit' : round(total_profit,2)+int(total_reward_profit),
            'my_rewards' : RewardHistory.objects.all().filter(user=request.user),
            'total_rewards' : int(total_reward_profit),
            'total_share' : round(total_profit,2),
            'terms_condition_text' : terms_condition.text.strip()
        }
        return render(request, 'management/sales_dashboard.html', context=context)

@login_required
def register_shopkeeper(request):
    if not SalesPerson.objects.get(user = request.user):
        return redirect("/")
    if request.method == 'POST':

        shopdetails = ShopDetails.objects.all().filter(shop_name = request.POST.get('shopName'))

        if shopdetails:
            return redirect("/sales")

        salesperson = SalesPerson.objects.get(user = request.user)

        discount_list = []
        
        purchase = request.POST.getlist('purchaseData[]')
        discounts = request.POST.getlist('discountData[]')

        for i in range(len(purchase)):
            discount = Discount.objects.create(total_purchase = int(purchase[i]),discount = int(discounts[i]))
            discount.save()
            discount_list.append(discount)

        # before 
        # invoice_number = "INV/BOFF/"+ str(1001 + len(ShopDetails.objects.all()))0
        # new invoice number goes below

        if(len(ShopDetails.objects.all()) - 607 < 10):
            invoice_number = "INV/BOFF/"+str(00) + str(len(ShopDetails.objects.all()) - 607+1)
        elif(len(ShopDetails.objects.all()) - 607 < 10):
            invoice_number = "INV/BOFF/"+str(0) + str(len(ShopDetails.objects.all()) - 607+1)
        else:
            invoice_number = "INV/BOFF/" + str(len(ShopDetails.objects.all()) - 607+1)

        salesperson = SalesPerson.objects.get(user = request.user)

        shop = ShopDetails.objects.create(
            created_by =  request.user,
            shop_name = request.POST.get('shopName'),
            owner_name = request.POST.get('ownerName'),
            gst_no = request.POST.get('gstNumber'),
            phone_number = request.POST.get('phoneNumber'),
            whatsapp_number = request.POST.get('whatsappNumber'),
            address = request.POST.get('address'),
            city = salesperson.city.city_name,
            minilocation = request.POST.get('minilocation'),
            email_address = request.POST.get('emailAddress'),
            business_category = Category.objects.get(id=int(request.POST.get('businessCategory'))),
            products = request.POST.get('products'),
            total_eligible_customer = request.POST.get('totalCustomers'),
            package_amount = request.POST.get('packageAmount'),
            transaction_id = request.POST.get('transactionId'),
            image_file1 = request.FILES["file1"].name if 'file1' in request.FILES else None,
            comment1 = request.POST.get('comment1', 'No Comments'),
            image_file2 = request.FILES['file2'].name if 'file2' in request.FILES else None,
            comment2 = request.POST.get('comment2', 'No Comments'),
            image_file3 = request.FILES['file3'].name if 'file3' in request.FILES else None,
            comment3 = request.POST.get('comment3', 'No Comments'),
            image_file4 = request.FILES['file4'].name if 'file4' in request.FILES else None,
            comment4 = request.POST.get('comment4', 'No Comments'),
            payment_verified = False,
            invoice_no = invoice_number,
            sales_profit = int(request.POST.get('packageAmount'))*((salesperson.share)/100.0)*0.82,
            forward_to_freelancer = True,
            latitude = request.POST.get('latitude'),
            longitude = request.POST.get('longitude')
        )

        if 'file1' in request.FILES:
            shop.image_file1.save(request.FILES["file1"].name, request.FILES["file1"])
        if 'file2' in request.FILES:
            shop.image_file2.save(request.FILES["file2"].name, request.FILES["file2"])
        if 'file3' in request.FILES:
            shop.image_file3.save(request.FILES["file3"].name, request.FILES["file3"])
        if 'file4' in request.FILES:
            shop.image_file4.save(request.FILES["file4"].name, request.FILES["file4"])
        
        shop.discounts.set(discount_list)
        
        shop.save()


        # create a username
        try:
            if User.objects.get(username=request.POST.get('ownerName').replace(" ","")):
                username = request.POST.get('ownerName').replace(" ","")+str(len(User.objects.all()))
        except :
            username = request.POST.get('ownerName').replace(" ","")

        # create the user
        user = User.objects.create_user(
            username=username,
            email= request.POST.get("emailAddress"),
            password="Hello@321"
        )
        user.is_staff=True 
        user.save()
        
        # create the shopkeeper
        shopkeeper = Shopkeeper.objects.create(
            user = user,
            mobile_number = request.POST.get('phoneNumber'),
            pwd = "Hello@321"
        )

        shopkeeper.save()

        shop.save()

        # send_invoice_and_credentials(request.POST.get('ownerName').replace(" ",""), "Hello@321", request.POST.get('shopName'), request.POST.get('emailAddress'))

        amount = int(request.POST.get('packageAmount'))
        
        # mail delivery for username, password
        send_credentials(
            request.POST.get('ownerName'), 
            request.POST.get('ownerName').replace(" ",""), 
            "Hello@321", 
            request.POST.get('emailAddress')
        )

        # mail delivery for invoice
        send_invoice(
            request.POST.get('ownerName'), 
            round(amount*0.82, 2), 
            round(amount*0.18, 2), 
            int(amount), 
            invoice_number, 
            request.POST.get('emailAddress')
        )

        # sms delivery for username, password
        send_username_password(
            request.POST.get('ownerName'), 
            request.POST.get('phoneNumber'), 
            request.POST.get('ownerName').replace(" ",""), 
            "Hello@321"
        )

        # sms delivery for invoice
        send_invoice_details(
            request.POST.get('ownerName'), 
            request.POST.get('phoneNumber'), 
            invoice_number, 
            request.POST.get('packageAmount')
        )

        # check if the salesperson made 10 deals of Rs. 199 in a day

        # fetch all the details which are not covered with the reward
        all_shop_details = ShopDetails.objects.all().filter(created_by=request.user, date_of_registration=datetime.date.today(), covered_under_reward=False, package_amount=199)

        reward_scheme = RewardScheme.objects.get(package=199)

        if len(all_shop_details)>=reward_scheme.total_sale:
            # give 100 Rs. Bonus to him with date
            total_reward = (len(all_shop_details)/reward_scheme.total_sale)*reward_scheme.total_rewards
            reward = RewardHistory.objects.create(
                user = request.user,
                note = "Earned a reward of Rs. "+str(total_reward)+" for making "+str(len(all_shop_details))+" sales in a Day.",
                reward = total_reward
            )
            reward.save()

            # make the those offers as covered_under_reward = True so that they are not selected next time

            for i in range(int(len(all_shop_details)/reward_scheme.total_sale)*reward_scheme.total_sale):
                all_shop_details[i].covered_under_reward = True
                all_shop_details[i].save()

        reward_scheme = RewardScheme.objects.get(package=2999)

        # check if the salesperson made 1 deal of 2999
        if int(request.POST.get('packageAmount')) == 2999:
            # give 200 Rs. Bonus to him with date
            reward = RewardHistory.objects.create(
                user = request.user,
                note = "Earned a reward of Rs."+str(reward_scheme.total_rewards)+" for making a 2999 Package sale.",
                reward = reward_scheme.total_rewards
            )

            reward.save()

            shop.covered_under_reward = True
            shop.save()

        # check if the total sale of this month is more than 50,000
        today = datetime.date.today()
        all_shop_details = ShopDetails.objects.all().filter(created_by=request.user, date_of_registration__month=today.month, covered_under_monthly_reward=False)
        
        this_month_total = 0

        reward_scheme = RewardScheme.objects.get(package=50000)

        for shop in all_shop_details:
            this_month_total += shop.package_amount
        
        if this_month_total>=50000:
            reward_amount = int(this_month_total/50000)*reward_scheme.total_rewards

            reward = RewardHistory.objects.create(
                user = request.user,
                note = "Earned a reward of Rs."+str(reward_amount)+" for making a Rs."+str(this_month_total)+" sale this month.",
                reward = reward_amount
            )

            reward.save()

            this_month_total_check = 0

            i=0

            for shop in all_shop_details:
                this_month_total_check += shop.package_amount

                if this_month_total_check > int(this_month_total):
                    i-=1
                    break
                elif this_month_total_check == int(this_month_total):
                    break
                else:
                    i+=1
            
            for j in range(i+1):
                all_shop_details[j].covered_under_monthly_reward = True
                all_shop_details[j].save()
        
        # now as the shop is registered, now register the same shop in the offer section 

        make_offer_without_img(shop.id)

        return render(request, 'management/shop-registration-success.html', {'shop_name' : request.POST.get('shopName')})
    
    salesperson = SalesPerson.objects.get(user = request.user)
    
    all_mini_location = MiniLocation.objects.all().filter(main_city = salesperson.city)
    
    context = {
        "all_mini_location" : all_mini_location,
        "pin" : salesperson.security_code,
        "categories" : Category.objects.all()
    }
    
    return render(request, 'management/shop-register.html', context=context)

def show_invoice(request, invoice_number):
    shop_details = ShopDetails.objects.get(invoice_no=invoice_number)
    return FileResponse(open('invoice/'+ shop_details.shop_name +'.pdf', 'rb'), content_type='application/pdf')

def shop_registration_successful(request):
    shop_name = "PineApple Inc."
    return render(request, 'management/shop-registration-success.html', {'shop_name' : shop_name})

def show_pdf(request):
    invoice_id = request.GET.get("invoice-number")
    shop = ShopDetails.objects.get(invoice_no=invoice_id)
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    p.setFont("Helvetica", 20, leading=None)
    p.setFillColorRGB(1, 0.35294117647, 0)

    p.drawString(270, 800, "Bharat")

    p.setFillColorRGB(0, 0, 0)
    p.drawString(330, 800, "Off")

    p.setFont("Helvetica", 15, leading=None)
    p.drawString(50, 780, "3rd Floor, Shop no-45, Magneto Mall, Labhandi Road, Raipur (C.G.) - 492002")

    p.line(10, 770, 585, 770)

    p.setFont("Helvetica-Bold", 15, leading=None)
    p.drawString(280, 730, "INVOICE")

    p.setFont("Helvetica", 12, leading=None)

    p.drawString(480, 715, "Date: "+str(shop.date_of_registration))
    p.drawString(420, 700, "GST No: 22FIAPS9006P1ZU")

    p.drawString(20, 670, "Invoice Number: "+invoice_id)

    p.drawString(20, 640, "Bill To:")
    p.drawString(20, 615, shop.shop_name+",")
    p.drawString(20, 600, shop.address+" - "+shop.city+",")
    p.drawString(20, 585, "Contact No - "+shop.phone_number)

    if len(shop.gst_no) > 3:
        p.drawString(20, 570, "GST No - "+shop.gst_no)
    
    p.line(30, 540, 565, 540)
    p.line(30, 500, 565, 500)
    p.line(30, 460, 565, 460)

    p.line(30, 540, 30, 460)
    p.line(565, 540, 565, 460 )

    p.line(450, 540, 450, 460 )
    p.line(70, 540, 70, 460 ) # line after S.No.


    p.line(400, 540, 400, 460 )
    p.line(350, 540, 350, 460 )

    p.drawString(35, 518, "S.No.")
    p.drawString(40, 478, "1.")

    p.drawString(360, 518, "QTY")
    p.drawString(370, 478, "1")

    p.drawString(410, 518, "Unit")
    p.drawString(415, 478, "Year")

    p.drawString(180, 518, "Description")
    p.drawString(480, 518, "Amount")

    p.setFont("Helvetica", 10, leading=None)


    p.drawString(80, 478, str(shop.package_amount)+" Package (1 Year Advertisement + Dashboard Support)")
    p.drawString(480, 478, str(round(shop.package_amount*0.82, 2))+" INR")

    p.setFont("Helvetica", 13, leading=None)

    p.drawString(440, 410, "Total: "+str(round(shop.package_amount*0.82, 2))+" INR")
    p.drawString(440, 390, "GST(18%): "+str(round(shop.package_amount*0.18, 2))+" INR")

    p.setFont("Helvetica-Bold", 13, leading=None)
    
    p.drawString(440, 370, "Grand Total: "+str(shop.package_amount)+" INR")


    p.setFont("Helvetica-Bold", 7, leading=None)

    p.drawString(30, 350, "Payment Terms: 100% Paid")

    p.drawString(30, 50, "This is computer generated invoice. No Signature is required.")


    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=invoice_id+'.pdf')

@login_required
def show_all_invoices(request):
    if request.user.is_superuser:
        all_shop_details = ShopDetails.objects.all()
        context = {
            "all_shop_details" : all_shop_details,
        }
        return render(request, "management/all_invoices.html", context)
    else:
        return redirect("/")

def raise_security_concern(request, id):
    user = User.objects.get(id=int(id))
    salesperson = SalesPerson.objects.get(user = user)
    salesperson.security_warning = True
    salesperson.save()

    user.is_active = False
    user.save()

    return redirect("/shop-registration")

@login_required
def freelancer_dashboard(request):
    freelancer = Freelancer.objects.get(user = request.user)

    all_salesperson_user = []
    
    for salesperson in freelancer.comes_under.all():
        all_salesperson_user.append(salesperson.user)

    all_shop_details = ShopDetails.objects.all().filter(created_by__in = all_salesperson_user).filter(date_of_registration__gt=freelancer.date_of_joining)

    context = {
        "all_shops" : all_shop_details,
    }

    return render(request, "management/freelancer-dashboard.html", context = context)

@login_required
def view_shop_details(request):
    shop_id = int(request.GET.get('shop-id'))
    shop = ShopDetails.objects.get(id=shop_id)

    comments = Designcomments.objects.all().filter(shopdetails=ShopDetails.objects.get(id=shop_id)).order_by("-datetime")

    context = {
        "shop" : shop,
        "comments": comments
    }
    return render(request, "management/view-shop-details.html", context=context)

def forward_to_freelancer(request):
    shop_id = int(request.GET.get("shop_id"))
    shop = ShopDetails.objects.get(id=shop_id)

    shop.forward_to_freelancer = True
    shop.save()

    return HttpResponse("Success")

def approve_design(request):
    print("CONTROLL HERE")
    shop_id = int(request.GET.get("shop_id"))
    shop = ShopDetails.objects.get(id=shop_id)
    salesperson = SalesPerson.objects.get(user=shop.created_by)

    shop.design_approved = True
    shop.save()

    offer = Files.objects.get(company_name = shop.shop_name)
    offer.img = shop.final_pamphlet
    offer.save()

    # create a offer

    # for Country
    # if shop.package_amount == 100000:
    #     offer = Files.objects.create(
    #         comes_under = shop.created_by,
    #         user = User.objects.get(email=shop.email_address),
    #         company_name=shop.shop_name,
    #         category = shop.business_category,
    #         heading = "Best Offer of the Month",
    #         phone_number = shop.phone_number,
    #         whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
    #         img = shop.final_pamphlet
    #     )
    #     cities = CityData.objects.all()
    #     minilocations = MiniLocation.objects.all()

    #     offer.city.set(cities)
    #     offer.MiniLocation.set(minilocations)

    #     offer.save()

    # # for State
    # if shop.package_amount == 10000:
    #     offer = Files.objects.create(
    #         comes_under = shop.created_by,
    #         user = User.objects.get(email=shop.email_address),
    #         company_name=shop.shop_name,
    #         category = shop.business_category,
    #         heading = "Best Offer of the Month",
    #         phone_number = shop.phone_number,
    #         whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
    #         img = shop.final_pamphlet
    #     )

    #     state = StateData.objects.get(cities=salesperson.city)
    #     cities = state.cities.all()
    #     minilocations = []

    #     for city in cities:
    #         minilocations += MiniLocation.objects.all().filter(main_city=city)
        
    #     offer.city.set(cities)
    #     offer.MiniLocation.set(minilocations)

    #     offer.save()


    # # for city
    # if shop.package_amount == 2999:
    #     offer = Files.objects.create(
    #         comes_under = shop.created_by,
    #         user = User.objects.get(email=shop.email_address),
    #         company_name=shop.shop_name,
    #         category = shop.business_category,
    #         heading = "Best Offer of the Month",
    #         phone_number = shop.phone_number,
    #         whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
    #         img = shop.final_pamphlet
    #     )

    #     cities = [salesperson.city,]
    #     minilocations = MiniLocation.objects.all().filter(main_city=salesperson.city)

    #     offer.city.set(cities)
    #     offer.MiniLocation.set(minilocations)

    #     offer.save()

    # # for Mini Location
    # if shop.package_amount == 199:
    #     offer = Files.objects.create(
    #         comes_under = shop.created_by,
    #         user = User.objects.get(email=shop.email_address),
    #         company_name=shop.shop_name,
    #         category = shop.business_category,
    #         heading = "Best Offer of the Month",
    #         phone_number = shop.phone_number,
    #         whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
    #         img = shop.final_pamphlet
    #     )

    #     cities = [salesperson.city,]
    #     minilocations = [MiniLocation.objects.get(name=shop.minilocation),]

    #     offer.city.set(cities)
    #     offer.MiniLocation.set(minilocations)

    #     offer.save()

    # # for Street vendors
    # if shop.package_amount == 99:
    #     offer = Files.objects.create(
    #         comes_under = shop.created_by,
    #         user = User.objects.get(email=shop.email_address),
    #         company_name=shop.shop_name,
    #         category = shop.business_category,
    #         heading = "Best Offer of the Month",
    #         phone_number = shop.phone_number,
    #         whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
    #         img = shop.final_pamphlet
    #     )

    #     cities = [salesperson.city,]
    #     minilocations = [MiniLocation.objects.get(name=shop.minilocation),]

    #     offer.city.set(cities)
    #     offer.MiniLocation.set(minilocations)

    #     offer.save()
    
    # # give reward to the freelancer

    

    # # create coupons

    # all_discount = shop.discounts.all()

    # for discount in all_discount:
    #     coupon = Coupon.objects.create(
    #         user = User.objects.get(email=shop.email_address),
    #         code = "GET" + str(discount.discount),
    #         offer = offer,
    #         total_coupon = shop.total_eligible_customer,
    #         minimum_purchase = discount.total_purchase,
    #         total_discount = discount.discount,
    #         end_date = datetime.now()+timedelta(days=365)
    #     )

    #     coupon.save()
    
    return HttpResponse("Success")

def make_offer_without_img(shop_id):
    # this function will be called from the register_shopkeeper() function
    default_design = DefaultDesign.objects.all()[0]

    shop_id = int(shop_id)
    shop = ShopDetails.objects.get(id=shop_id)
    salesperson = SalesPerson.objects.get(user=shop.created_by)

    shop.design_approved = False
    shop.save()

    # create a offer

    # for Country
    if shop.package_amount == 100000:
        offer = Files.objects.create(
            comes_under = shop.created_by,
            user = User.objects.get(email=shop.email_address),
            company_name=shop.shop_name,
            category = shop.business_category,
            heading = "Best Offer of the Month",
            phone_number = shop.phone_number,
            whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
            img = default_design.design,
            slider_image1 = shop.image_file2,
            slider_image2 = shop.image_file3,
            slider_image3 = shop.image_file4,
            location = "https://maps.google.com/?q="+str(shop.latitude)+str(shop.longitude)
        )
        cities = CityData.objects.all()
        minilocations = MiniLocation.objects.all()

        offer.city.set(cities)
        offer.MiniLocation.set(minilocations)

        offer.active = True

        offer.save()

    # for State
    if shop.package_amount == 10000:
        offer = Files.objects.create(
            comes_under = shop.created_by,
            user = User.objects.get(email=shop.email_address),
            company_name=shop.shop_name,
            category = shop.business_category,
            heading = "Best Offer of the Month",
            phone_number = shop.phone_number,
            whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
            img = default_design.design,
            slider_image1 = shop.image_file2,
            slider_image2 = shop.image_file3,
            slider_image3 = shop.image_file4,
            location = "https://maps.google.com/?q="+str(shop.latitude)+str(shop.longitude)
        )

        state = StateData.objects.get(cities=salesperson.city)
        cities = state.cities.all()
        minilocations = []

        for city in cities:
            minilocations += MiniLocation.objects.all().filter(main_city=city)
        
        offer.city.set(cities)
        offer.MiniLocation.set(minilocations)

        offer.active = True

        offer.save()


    # for city
    if shop.package_amount == 2999:
        offer = Files.objects.create(
            comes_under = shop.created_by,
            user = User.objects.get(email=shop.email_address),
            company_name=shop.shop_name,
            category = shop.business_category,
            heading = "Best Offer of the Month",
            phone_number = shop.phone_number,
            whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
            img = default_design.design,
            slider_image1 = shop.image_file2,
            slider_image2 = shop.image_file3,
            slider_image3 = shop.image_file4,
            location = "https://maps.google.com/?q="+str(shop.latitude)+str(shop.longitude)
        )

        cities = [salesperson.city,]
        minilocations = MiniLocation.objects.all().filter(main_city=salesperson.city)

        offer.city.set(cities)
        offer.MiniLocation.set(minilocations)

        offer.active = True

        offer.save()

    # for Mini Location
    if shop.package_amount == 199:
        offer = Files.objects.create(
            comes_under = shop.created_by,
            user = User.objects.get(email=shop.email_address),
            company_name=shop.shop_name,
            category = shop.business_category,
            heading = "Best Offer of the Month",
            phone_number = shop.phone_number,
            whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
            img = default_design.design,
            slider_image1 = shop.image_file2,
            slider_image2 = shop.image_file3,
            slider_image3 = shop.image_file4,
            location = "https://maps.google.com/?q="+str(shop.latitude)+str(shop.longitude)
        )

        cities = [salesperson.city,]
        minilocations = [MiniLocation.objects.get(name=shop.minilocation),]

        offer.city.set(cities)
        offer.MiniLocation.set(minilocations)

        offer.active = True

        offer.save()

    # for Mini Location - 299
    if shop.package_amount == 299:
        offer = Files.objects.create(
            comes_under = shop.created_by,
            user = User.objects.get(email=shop.email_address),
            company_name=shop.shop_name,
            category = shop.business_category,
            heading = "Best Offer of the Month",
            phone_number = shop.phone_number,
            whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
            img = default_design.design,
            slider_image1 = shop.image_file2,
            slider_image2 = shop.image_file3,
            slider_image3 = shop.image_file4,
            location = "https://maps.google.com/?q="+str(shop.latitude)+str(shop.longitude)
        )

        cities = [salesperson.city,]
        minilocations = [MiniLocation.objects.get(name=shop.minilocation),]

        offer.city.set(cities)
        offer.MiniLocation.set(minilocations)

        offer.active = True

        offer.save()

    # for Street vendors
    if shop.package_amount == 99:
        offer = Files.objects.create(
            comes_under = shop.created_by,
            user = User.objects.get(email=shop.email_address),
            company_name=shop.shop_name,
            category = shop.business_category,
            heading = "Best Offer of the Month",
            phone_number = shop.phone_number,
            whatsapp_link = "https://wa.me/91"+str(shop.whatsapp_number),
            img = default_design.design,
            slider_image1 = shop.image_file2,
            slider_image2 = shop.image_file3,
            slider_image3 = shop.image_file4,
            location = "https://maps.google.com/?q="+str(shop.latitude)+str(shop.longitude)
        )

        cities = [salesperson.city,]
        minilocations = [MiniLocation.objects.get(name=shop.minilocation),]

        offer.city.set(cities)
        offer.MiniLocation.set(minilocations)

        offer.active = True

        offer.save()
    
    # give reward to the freelancer

    

    # create coupons

    all_discount = shop.discounts.all()

    for discount in all_discount:
        coupon = Coupon.objects.create(
            user = User.objects.get(email=shop.email_address),
            code = "GET" + str(discount.discount),
            offer = offer,
            total_coupon = shop.total_eligible_customer,
            minimum_purchase = discount.total_purchase,
            total_discount = discount.discount,
            end_date = datetime.datetime.now()+timedelta(days=365)
        )

        coupon.save()
    
    return HttpResponse("Success")

def reject_with_comment(request):
    shop_id = int(request.POST.get("shop_id"))
    comment = request.POST.get("comment")

    design_comment = Designcomments.objects.create(
        shopdetails = ShopDetails.objects.get(id=shop_id),
        user = request.user,
        comment = comment
    )

    design_comment.save()

    return redirect("/view-shop-details/?shop-id="+str(shop_id))

def view_shop_details_freelancer(request):
    shop_id = int(request.GET.get("shop_id"))
    shopdetails = ShopDetails.objects.get(id=shop_id)

    comments = Designcomments.objects.all().filter(shopdetails=ShopDetails.objects.get(id=shop_id)).order_by("-datetime")

    context = {
        "shop" : shopdetails,
        "comments" : comments,
    }
    return render(request, "management/view-shop-details-freelancer.html", context = context)

def upload_design(request):
    shop_id = int(request.POST.get("shop_id"))
    comment = request.POST.get("comment")

    shopDetails = ShopDetails.objects.get(id=shop_id)

    if 'design' in request.FILES:
        shopDetails.final_pamphlet.save(request.FILES["design"].name, request.FILES["design"])
    
    shopDetails.save()
    
    design_comment = Designcomments.objects.create(
        shopdetails = ShopDetails.objects.get(id=shop_id),
        user = request.user,
        comment = comment
    )

    design_comment.save()
    return redirect("/view-shop-details-freelancer/?shop_id="+str(shop_id))

def update_social_media_links(request):
    offer = Files.objects.get(user=request.user)

    offer.facebook_link = request.POST.get("facebookUrl")
    offer.instagram_link = request.POST.get("instagramUrl")
    offer.youtube_link = request.POST.get("youtubeUrl")
    offer.location = request.POST.get("gmapUrl")

    offer.save()

    return redirect("/dashboard")

def image_editing(request):
    pamphlet = PamphletDesign.objects.all()[0]
    
    offer = Files.objects.get(user=request.user)

    my_image = Image.open(pamphlet.design)

    title_font = ImageFont.truetype(pamphlet.font_file, 40)

    w,h = title_font.getsize(offer.company_name)
    W = 750
    H = 800

    image_editable = ImageDraw.Draw(my_image)

    # image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
    image_editable.text(((W-w)/2,(h)/2), offer.company_name, font=title_font, fill="black")

    in_mem_file = io.BytesIO()

    my_image.save(in_mem_file, format=my_image.format)

    new_design = DownloadedDesigns.objects.create(user = request.user, base_pamphlet = pamphlet)
    new_design.save()

    new_design.design.save("custom-design.png",ContentFile(in_mem_file.getvalue()),save=True)

    response = FileResponse(pamphlet.design)

    return response

def make_coupons_manually(request):
    all_coupons = Coupon.objects.all()

    for coupon in all_coupons:
        pass
    pass

def assign_slider_image_script(request):
    all_shop_details = ShopDetails.objects.all()

    print("Total length: ", len(all_shop_details))

    try:
        for i in range(len(all_shop_details)):
            ad = Files.objects.all().filter(company_name = all_shop_details[i].shop_name)[0]
            if ad:
                ad.slider_image1 = all_shop_details[i].image_file2
                ad.slider_image2 = all_shop_details[i].image_file3
                ad.slider_image3 = all_shop_details[i].image_file4
                ad.save()
                print("Saved the ad for ", all_shop_details[i].shop_name)
            else:
                print("No ad exist for ", all_shop_details[i].shop_name)

    except:
        print("Exception occured for ", all_shop_details[i].shop_name)

def upload_slider_images(request):
    ad_id = int(request.POST.get("ad_id"))

    ad = Files.objects.get(id=ad_id)

    if 'sliderimage1' in request.FILES:
            ad.slider_image1.save(request.FILES["sliderimage1"].name, request.FILES["sliderimage1"])
    if 'sliderimage2' in request.FILES:
            ad.slider_image2.save(request.FILES["sliderimage2"].name, request.FILES["sliderimage2"])
    if 'sliderimage3' in request.FILES:
            ad.slider_image3.save(request.FILES["sliderimage3"].name, request.FILES["sliderimage3"])
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))