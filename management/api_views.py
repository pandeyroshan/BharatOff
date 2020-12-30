from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

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
    )


from django.views.decorators.csrf import csrf_exempt
from math import sin, cos, sqrt, atan2, radians
import random
import datetime
from django.contrib.auth.models import User
from wsgiref.util import FileWrapper
import mimetypes



@api_view(['GET'])
@permission_classes((AllowAny,))
def all_categories(request):
    categories = Category.objects.all()
    context = {

    }
    for data in categories:
        context[data.id] = data.name
    return Response(context)


@api_view(['POST'])
@permission_classes((AllowAny,))
def all_advertisement(request):
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
    
    visitor_object = Visitors.objects.get(city = nearest_city)
    visitor_object.counter += 1
    visitor_object.save()

    nearby_location_json = {}

    for data in nearby_location:
        nearby_location_json[data.id] = data.name

    location_information = {
        "nearest_location_id" : nearest_location.id,
        "nearest_location_name" : nearest_location.name,
        "main_city_id" : nearest_location.main_city.id,
        "main_city_name" : nearest_location.main_city.city_name,
        "nearby_locations" : nearby_location_json
    }

    all_ads_json = {}

    for data in all_ads:
        current_ad = {}
        current_ad["company_name"] = data.company_name
        current_ad["heading"] = data.heading
        current_ad["phone_number"] = data.phone_number
        current_ad["whatsapp_link"] = data.whatsapp_link
        current_ad["google_location"] = data.location
        current_ad["facebook_link"] = data.facebook_link
        current_ad["instagram_link"] = data.instagram_link
        current_ad["youtube_link"] = data.youtube_link
        current_ad["image_link"] = str(data.real_image)

        all_ads_json[data.id] = current_ad
    
    print(type(all_ads_json))
    
    context = {
        "all_ads" : all_ads_json,
        "location_information" : location_information,
    }
    return Response(context)

@api_view(['GET'])
def get_all_states(request):
    context = {}
    for data in StateData.objects.all():
        context[data.id] = data.state_name
    return Response(context)

@api_view(['POST'])
def get_cities(request):
    context = {}
    cities = StateData.objects.get(id = int(request.POST.get('id'))).cities.all()
    for data in cities:
        context[data.id] = data.city_name
    return Response(context)

@api_view(['POST'])
def get_minilocation(request):
    context = {}
    minilocations = MiniLocation.objects.all().filter(main_city = CityData.objects.get(id = int(request.POST.get('id'))))
    for data in minilocations:
        context[data.id] = data.name
    return Response(context)

@api_view(['POST'])
def get_ad_detail(request):
    context = {}
    ad = Files.objects.get(id=int(request.POST.get("id")))
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
    
    context["company_name"] = ad.company_name
    context["heading"] = ad.heading
    context["phone_number"] = ad.phone_number
    context["whatsapp_link"] = ad.whatsapp_link
    context["google_location"] = ad.location
    context["facebook_link"] = ad.facebook_link
    context["instagram_link"] = ad.instagram_link
    context["youtube_link"] = ad.youtube_link
    context["image_link"] = str(ad.real_image)

    return Response(context)

@api_view(['POST'])
def get_search_result(request):
    lat = request.POST.get("lat")
    lon = request.POST.get("lon")

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

    raw_keywords = request.POST.get("keywords")

    keywords = raw_keywords.split(",")

    for i in range(len(keywords)):
        keywords[i] = keywords[i].strip()

    keywords = [x.lower() for x in keywords]
    
    all_offers = Files.objects.all().filter(city = nearest_location.main_city)

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
    
    for i in range(len(searched_offers)):
        if searched_offers[i].active_image == 0:
            searched_offers[i].real_image = searched_offers[i].img
        elif searched_offers[i].active_image == 1:
            searched_offers[i].real_image = searched_offers[i].img1
        elif searched_offers[i].active_image == 2:
            searched_offers[i].real_image = searched_offers[i].img2
        elif searched_offers[i].active_image == 3:
            searched_offers[i].real_image = searched_offers[i].img3
        elif searched_offers[i].active_image == 4:
            searched_offers[i].real_image = searched_offers[i].img4
        elif searched_offers[i].active_image == 5:
            searched_offers[i].real_image = searched_offers[i].img5
        elif searched_offers[i].active_image == 6:
            searched_offers[i].real_image = searched_offers[i].img6
        elif searched_offers[i].active_image == 7:
            searched_offers[i].real_image = searched_offers[i].img7
        elif searched_offers[i].active_image == 8:
            searched_offers[i].real_image = searched_offers[i].img8
        elif searched_offers[i].active_image == 9:
            searched_offers[i].real_image = searched_offers[i].img9

    all_ads_json = {}

    for data in searched_offers:
        current_ad = {}
        current_ad["company_name"] = data.company_name
        current_ad["heading"] = data.heading
        current_ad["phone_number"] = data.phone_number
        current_ad["whatsapp_link"] = data.whatsapp_link
        current_ad["google_location"] = data.location
        current_ad["facebook_link"] = data.facebook_link
        current_ad["instagram_link"] = data.instagram_link
        current_ad["youtube_link"] = data.youtube_link
        current_ad["image_link"] = str(data.real_image)

        all_ads_json[data.id] = current_ad
    return Response(all_ads_json)