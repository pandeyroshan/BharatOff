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
        print(request.POST)
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')

        min_distance = 100000005

        print(lat,lon)

        all_city = CityData.objects.all()

        R = 6373.0

        for city in all_city:
            lat1 = radians(float(lat))
            lon1 = radians(float(lon))
            lat2 = radians(city.lat)
            lon2 = radians(city.lon)

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c

            if distance < min_distance:
                min_distance = distance
                nearest_city = city
        print(nearest_city)
    
    address = Address.objects.all()[0]

    nearby_location = MiniLocation.objects.all().filter(main_city=nearest_city)
    
    states = StateData.objects.all()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    
    counter = WebCounter.objects.get(id=1)
    counter.visit += random.randint(0,5)
    counter.save()

    context = {
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
    context = {
        'offers' : offers,
        'cities' : CityData.objects.all(),
        'city' : CityData.objects.get(id=int(id)),
        'address' : Address.objects.all()[0],
        'states' : states
    }

    visitor_object = Visitors.objects.get(city = CityData.objects.get(id=int(id)))
    visitor_object.counter += 1
    visitor_object.save()

    return render(request,'management/location.html',context)

def single(reqeust, id):
    ad = Files.objects.get(id=id)
    states = StateData.objects.all()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    
    context = {
        'ad': ad,
        'states' : states,
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