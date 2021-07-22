from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import (
    CityData, 
    Address, 
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
    ShopDetails
)

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

        context = {
            'total_ads' : len(my_ads),
            'active_ads' : len(Files.objects.all().filter(user=request.user, active=True)),
            'city_count' : len(my_city),
            'counter' : counter,
            'ads' : my_ads,
            'my_city' : my_city
        }
        messages.success(request, 'Your password was updated successfully!')
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
        try:
            context['coupon'] = Coupon.objects.get(offer = Files.objects.get( id = int(id)))
        except:
            pass
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
        
        return render(request, 'management/image_resources.html', {'all_images': images})
    if request.user.is_staff:
        all_images = Resources.objects.all()
        return render(request, 'management/image_resources.html', {'all_images': all_images})
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
    coupon, _ = Coupon.objects.get_or_create(user = request.user, offer = Files.objects.get( id = int(request.POST.get('offer_id'))))
    coupon.code = request.POST.get('code')
    coupon.start_date = request.POST.get('start-date')
    coupon.end_date = request.POST.get('end-date')
    coupon.total_coupon = request.POST.get('total-coupon')

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
            profit = (all_shop_details[i].package_amount * 0.82)*((salesperson.share)/100.0)
            total_profit+=profit
            all_shop_details[i].profit = int(profit)
        
        verified_payements = 0
        
        for shop in all_shop_details:
            if shop.payment_verified:
                verified_payements+=1
        context = {
            'all_shops' : all_shop_details,
            'total_advertisement' : len(all_shop_details),
            'total_verified_payments' : verified_payements,
            'total_unverified_payments' : len(all_shop_details) - verified_payements,
            'total_profit' : int(total_profit)
        }
        return render(request, 'management/sales_dashboard.html', context=context)

@login_required
def register_shopkeeper(request):
    if not SalesPerson.objects.get(user = request.user):
        return redirect("/")
    if request.method == 'POST':

        discount_list = []
        
        purchase = request.POST.getlist('purchaseData[]')
        discounts = request.POST.getlist('discountData[]')

        for i in range(len(purchase)):
            discount = Discount.objects.create(total_purchase = int(purchase[i]),discount = int(discounts[i]))
            discount.save()
            discount_list.append(discount)

        invoice_number = "IN"+ str(date.today()).replace("-", "") + str(len(ShopDetails.objects.all()))

        shop = ShopDetails.objects.create(
            created_by =  request.user,
            shop_name = request.POST.get('shopName'),
            owner_name = request.POST.get('ownerName'),
            gst_no = request.POST.get('gstNumber'),
            phone_number = request.POST.get('phoneNumber'),
            whatsapp_number = request.POST.get('whatsappNumber'),
            address = request.POST.get('address'),
            city = request.POST.get('city'),
            email_address = request.POST.get('emailAddress'),
            business_category = request.POST.get('businessCategory'),
            products = request.POST.get('products'),
            total_eligible_customer = request.POST.get('totalCustomers'),
            package_amount = request.POST.get('packageAmount'),
            transaction_id = request.POST.get('transactionId'),
            image_file1 = request.FILES['file1'].name if 'file1' in request.FILES else None,
            comment1 = request.POST.get('comment1', 'No Comments'),
            image_file2 = request.FILES['file2'].name if 'file2' in request.FILES else None,
            comment2 = request.POST.get('comment2', 'No Comments'),
            image_file3 = request.FILES['file3'].name if 'file3' in request.FILES else None,
            comment3 = request.POST.get('comment3', 'No Comments'),
            image_file4 = request.FILES['file4'].name if 'file4' in request.FILES else None,
            comment4 = request.POST.get('comment4', 'No Comments'),
            payment_verified = False,
            invoice_no = invoice_number
        )
        shop.discounts.set(discount_list)
        shop.save()

        user = User.objects.create_user(
            username=request.POST.get('ownerName').replace(" ",""),
            password="Hello@321"
        )
        user.save()

        shopkeeper = Shopkeeper.objects.create(
            user = user,
            mobile_number = request.POST.get('phoneNumber'),
            pwd = "Hello@321",
        )

        shopkeeper.save()

        # create the pdf of the invoice
        pdf = create_invoice(
            request.POST.get('shopName'), 
            request.POST.get('address'), 
            request.POST.get('phoneNumber'), 
            request.POST.get('gstNumber', 'Not Available'),
            request.POST.get('packageAmount')+" Package", 
            invoice_number,
            int(request.POST.get('packageAmount'))
        )

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

        return render(request, 'management/shop-registration-success.html', {'shop_name' : request.POST.get('shopName')})

    return render(request, 'management/shop-register.html')

def show_invoice(request, invoice_number):
    shop_details = ShopDetails.objects.get(invoice_no=invoice_number)
    return FileResponse(open('invoice/'+ shop_details.shop_name +'.pdf', 'rb'), content_type='application/pdf')

def shop_registration_successful(request):
    shop_name = "PineApple Inc."
    return render(request, 'management/shop-registration-success.html', {'shop_name' : shop_name})

def show_pdf(request):
    pdf = create_invoice("ABC Shop", "JP Nagar, Rewa - MP", "+91 9752315423","GSTIN1212112","199 Package", "IN20210706001" ,199)
    filename = "sample_pdf.pdf"

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response