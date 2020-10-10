from django.shortcuts import render, redirect
from .models import Files
from .models import CityData, Address, StateData, Visitors, Files, Messages, WebCounter, MiniLocation
from django.views.decorators.csrf import csrf_exempt
from math import sin, cos, sqrt, atan2, radians
import random
# Create your views here.

@csrf_exempt
def home(request):
    address = Address.objects.all()[0]
    states = StateData.objects.all()
    print(states.query)

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
    
    print(nearest_location)

    nearest_city = nearest_location.main_city

    address = Address.objects.all()[0]

    nearby_location = MiniLocation.objects.all().filter(main_city=nearest_city)
    
    states = StateData.objects.all()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    
    counter = WebCounter.objects.get(id=1)
    counter.visit += random.randint(0,5)
    counter.save()

    context = {
        'nearest_location' : nearest_location,
        'offers' : Files.objects.all().filter(city = nearest_city),
        'cities' : CityData.objects.all(),
        'city' : nearest_city,
        'address' : address,
        'states' : states,
        'counter' : counter,
        'nearby_location' : nearby_location
    }

    visitor_object = Visitors.objects.get(city = nearest_city)
    visitor_object.counter += 1
    visitor_object.save()

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
    minilocation = MiniLocation.objects.get(id=id)
    all_ads = Files.objects.all().filter(MiniLocation = minilocation)

    counter = WebCounter.objects.get(id=1)
    counter.visit += random.randint(0,5)
    counter.save()

    print(minilocation.main_city)

    nearby_location = MiniLocation.objects.all().filter(main_city = minilocation.main_city)

    context = {
        'offers' : all_ads,
        'cities' : CityData.objects.all(),
        'city' : CityData.objects.get(id=int(id)),
        'address' : Address.objects.all()[0],
        'states' : StateData.objects.all(),
        'counter' : counter,
        'nearby_location' : nearby_location
    }
    return render(request, 'management/location.html',context)

def single(reqeust, id):
    ad = Files.objects.get(id=id)
    states = StateData.objects.all()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    
    context = {
        'ad': ad,
        'states' : states,
        'address' : Address.objects.all()[0],
    }
    return render(reqeust,'management/single.html', context)

def contact(request):
    print(request.POST)
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

        for ad in my_ads:
            all_city = ad.city.all()
            for city in all_city:
                if city not in my_city:
                    my_city.append(city)
        
        print(my_city)

        counter = 0

        for city in my_city:
            counter += Visitors.objects.get(city=city).counter
        
        print(counter)

        context = {
            'total_ads' : len(my_ads),
            'active_ads' : len(Files.objects.all().filter(user=request.user, active=True)),
            'city_count' : len(my_city),
            'counter' : counter,
            'ads' : my_ads,
            'my_city' : my_city
        }
        return render(request,'management/dashboard.html', context)
    else:
        return redirect('/')