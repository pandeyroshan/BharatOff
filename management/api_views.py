from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import random
from users.models import UserProfile, DeviceID
from management.models import Category
from django.contrib.auth.models import User
from . import sms_delivery

from .models import (
    CityData, 
    Address,
    ShopDetails, 
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
    PaymentIssue,
    EnquiryLog
    )
from .views import schedule_refresh

from users.models import CustomerLogin, MonthlyWinner
import string

from django.views.decorators.csrf import csrf_exempt
from math import sin, cos, sqrt, atan2, radians
import random
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from wsgiref.util import FileWrapper
import mimetypes

from users.models import UserNotification


@api_view(['GET'])
@permission_classes((AllowAny,))
def all_categories(request):
    categories = Category.objects.all()
    context = {
        "message" : "success",
        "data" : []
    }
    for data in categories:
        context["data"].append(
            {
                "id" : data.id,
                "name" : data.name,
                "image" : str(data.img)
            }
        )
    return Response(context)


@api_view(['POST'])
@permission_classes((AllowAny,))
def all_advertisement(request):
    schedule_refresh()
    lat = request.POST.get('lat')
    lon = request.POST.get('lon')

    user_id = int(request.POST.get("user_id"))

    user = User.objects.get(id=user_id)

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

    nearby_location = MiniLocation.objects.all().filter(main_city=nearest_city)

    print(nearby_location)
    
    states = StateData.objects.all()

    for i in range(len(states)):
        states[i].all_city = states[i].cities.all()
    
    counter = WebCounter.objects.get(id=1)
    counter.visit += random.randint(0,5)
    counter.save()

    all_ads = Files.objects.all().filter(MiniLocation=nearest_location, active=True)

    print(all_ads)

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

    all_ads_json = []

    for data in all_ads:
        current_ad = {}
        current_ad["id"] = data.id
        current_ad["company_name"] = data.company_name
        current_ad["heading"] = data.heading
        current_ad["phone_number"] = data.phone_number
        current_ad["whatsapp_link"] = data.whatsapp_link
        current_ad["google_location"] = data.location
        current_ad["facebook_link"] = data.facebook_link
        current_ad["instagram_link"] = data.instagram_link
        current_ad["youtube_link"] = data.youtube_link
        current_ad["image_link"] = str(data.real_image)
        current_ad["rating"] = str(data.rating)

        current_ad["coupons"] = []

        all_coupons = Coupon.objects.all().filter(offer=data)

        coupon_history = CouponHistory.objects.all().filter(user=user)

        for coupon in all_coupons:
            new_coupon_detail = {}
            new_coupon_detail["coupon_id"] = coupon.id
            new_coupon_detail["coupon_code"] = coupon.code
            new_coupon_detail["minimum_purchase"] = coupon.minimum_purchase
            new_coupon_detail["total_discount"] = coupon.total_discount
            new_coupon_detail["is_active"] = coupon.active
            new_coupon_detail["last_date"] = coupon.end_date

            # check the coupon status weather it is scratched or not

            is_scratched = False
            scratch_status = "NA"

            for history in coupon_history:
                if history.coupon.id == coupon.id:
                    is_scratched = True

                    if history.status:
                        scratch_status = "WINNER"
                    else:
                        scratch_status = "NOT_A_WINNER"
            
            new_coupon_detail["is_scratched"] = is_scratched
            new_coupon_detail["scratch_status"] = scratch_status

            current_ad["coupons"].append(new_coupon_detail)

        all_ads_json.append(current_ad)

        print(current_ad)

    context = {
        "message" : "success",
        "data" : all_ads_json
    }
    return Response(context)

@api_view(['GET'])
def get_all_states(request):
    context = {
        "message" : "success",
        "data" : []
    }
    for data in StateData.objects.all():
        context["data"].append({
            "id" : data.id,
            "name" : data.state_name
        })
    return Response(context)

@api_view(['POST'])
def get_cities(request):
    context = {
        "message" : "success",
        "data" : []
    }
    cities = StateData.objects.get(id = int(request.POST.get('id'))).cities.all()
    for data in cities:
        context["data"].append(
            {
                "id" : data.id,
                "name" : data.city_name
            }
        )
    return Response(context)

@api_view(['POST'])
def get_minilocation(request):
    context = {
        "message" : "success",
        "data" : []
    }
    minilocations = MiniLocation.objects.all().filter(main_city = CityData.objects.get(id = int(request.POST.get('id'))))
    for data in minilocations:
        context["data"].append(
            {
                "id" : data.id,
                "name" : data.name,
                "lat" : data.lat,
                "lon" : data.lon,
            }
        )
    return Response(context)

@api_view(['POST'])
def get_ad_detail(request):
    context = {
        "message" : "success",
        "data" : []
    }
    ad = Files.objects.get(id=int(request.POST.get("ad_id")))
    user = User.objects.get(id = int(request.POST.get("user_id")))

    shop_detail = ShopDetails.objects.all().filter(shop_name=ad.company_name)[0]

    print(shop_detail.owner_name)

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
    
    context["data"].append({})

    context["data"][0]["id"] = ad.id
    context["data"][0]["company_name"] = ad.company_name
    context["data"][0]["heading"] = ad.heading
    context["data"][0]["phone_number"] = ad.phone_number
    context["data"][0]["whatsapp_link"] = ad.whatsapp_link
    context["data"][0]["google_location"] = ad.location
    context["data"][0]["facebook_link"] = ad.facebook_link
    context["data"][0]["instagram_link"] = ad.instagram_link
    context["data"][0]["youtube_link"] = ad.youtube_link
    context["data"][0]["image_link"] = str(ad.real_image)
    context["data"][0]["slider_image1_link"] = str(ad.slider_image1)
    context["data"][0]["slider_image2_link"] = str(ad.slider_image1)
    context["data"][0]["slider_image3_link"] = str(ad.slider_image1)
    context["data"][0]["rating"] = str(ad.rating)

    if shop_detail:
        context["data"][0]["shopkeeper_name"] = str(shop_detail.owner_name)
        context["data"][0]["address"] = str(shop_detail.address)
        context["data"][0]["products"] = str(shop_detail.products)

    context["data"][0]["coupon"] = []

    all_coupons = Coupon.objects.all().filter(offer=ad)

    coupon_history = CouponHistory.objects.all().filter(user=user)

    print(coupon_history)

    for coupon in all_coupons:
        new_coupon_detail = {}
        new_coupon_detail["coupon_id"] = coupon.id
        new_coupon_detail["coupon_code"] = coupon.code
        new_coupon_detail["minimum_purchase"] = coupon.minimum_purchase
        new_coupon_detail["total_discount"] = coupon.total_discount
        new_coupon_detail["is_active"] = coupon.active
        new_coupon_detail["last_date"] = coupon.end_date

        # check the coupon status weather it is scratched or not

        is_scratched = False
        scratch_status = "NA"

        for history in coupon_history:
            if history.coupon.id == coupon.id:
                is_scratched = True

                if history.status:
                    scratch_status = "WINNER"
                else:
                    scratch_status = "NOT_A_WINNER"
        
        new_coupon_detail["is_scratched"] = is_scratched
        new_coupon_detail["scratch_status"] = scratch_status

        context["data"][0]["coupon"].append(new_coupon_detail)

    return Response(context)

@api_view(['POST'])
def get_search_result(request):
    lat = request.POST.get("lat")
    lon = request.POST.get("lon")

    user = User.objects.get(id = int(request.POST.get("user_id")))

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

    raw_keywords_from_user = request.POST.get("keywords")

    searched_keywords = raw_keywords_from_user.split(",")

    for i in range(len(searched_keywords)):
        searched_keywords[i] = searched_keywords[i].strip()

    searched_keywords = [x.lower() for x in searched_keywords]
    
    all_offers = Files.objects.all().filter(city = nearest_location.main_city, active=True)

    searched_offers = []

    for offer in all_offers:
        raw_keywords = offer.keywords

        available_keywords = raw_keywords.split(",")

        available_keywords = [x.lower() for x in available_keywords]

        for i in range(len(available_keywords)):
            available_keywords[i] = available_keywords[i].strip()
        
        for key in searched_keywords:
            if key in available_keywords:
                searched_offers.append(offer)
                break
        
        if raw_keywords_from_user.lower() == offer.company_name.lower():
            searched_offers.append(offer)

        for keyword in searched_keywords:
            if keyword in list(map(str.lower, offer.company_name.split(" "))):
                searched_offers.append(offer)
                break
            
            try:
                shop_detail = ShopDetails.objects.all().filter(shop_name=offer.company_name)[0]

                shop_detail_product_list = list(map(str.lower, shop_detail.products.split(",")))

                for i in range(len(shop_detail_product_list)):
                    shop_detail_product_list[i] = shop_detail_product_list[i].strip()

                if keyword in shop_detail_product_list:
                    searched_offers.append(offer)
                    break       
            except:
                print("NO SHOP DETAILS EXIST")    
            
            if keyword == offer.category.name.lower():
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

    context = {
        "message" : "success",
        "data" : []
    }

    coupon_history = CouponHistory.objects.all().filter(user=user)

    for data in searched_offers:
        current_ad = {}
        current_ad["id"] = data.id
        current_ad["company_name"] = data.company_name
        current_ad["heading"] = data.heading
        current_ad["phone_number"] = data.phone_number
        current_ad["whatsapp_link"] = data.whatsapp_link
        current_ad["google_location"] = data.location
        current_ad["facebook_link"] = data.facebook_link
        current_ad["instagram_link"] = data.instagram_link
        current_ad["youtube_link"] = data.youtube_link
        current_ad["image_link"] = str(data.real_image)
        current_ad["rating"] = str(data.rating)

        current_ad["coupons"] = []

        all_coupons = Coupon.objects.all().filter(offer=data)

        for coupon in all_coupons:
            new_coupon_detail = {}
            new_coupon_detail["coupon_id"] = coupon.id
            new_coupon_detail["coupon_code"] = coupon.code
            new_coupon_detail["minimum_purchase"] = coupon.minimum_purchase
            new_coupon_detail["total_discount"] = coupon.total_discount
            new_coupon_detail["is_active"] = coupon.active
            new_coupon_detail["last_date"] = coupon.end_date

            # check the coupon status weather it is scratched or not

            is_scratched = False
            scratch_status = "NA"

            for history in coupon_history:
                if history.coupon.id == coupon.id:
                    is_scratched = True

                    if history.status:
                        scratch_status = "WINNER"
                    else:
                        scratch_status = "NOT_A_WINNER"
            
            new_coupon_detail["is_scratched"] = is_scratched
            new_coupon_detail["scratch_status"] = scratch_status

            current_ad["coupons"].append(new_coupon_detail)
        
        context["data"].append(current_ad)
    return Response(context)

@api_view(['POST'])
def rate_ad(request):
    rating = request.POST.get('rating')
    ad_id = request.POST.get('ad_id')
    user_id = request.POST.get('user_id')

    if not rating:
        return Response({"message":"Rating not given"})
    if not ad_id:
        return Response({"message":"Ad id not given"})
    if not user_id:
        return Response({"message":"User id not given"})

    print(user_id)

    user = User.objects.get(id = int(user_id))

    ad = Files.objects.get(id = int(ad_id))
    print(ad.rated_by.all())
    if user not in ad.rated_by.all():
        ad.rating = (ad.rating+int(rating))/2.0
        ad.rated_by.add(user)
    else:
        return Response({
            "message" : "Already rated."
        })
    ad.save()

    return Response({
        "message" : "Success",
        "data" : [
            {"new_rating" : ad.rating}
        ]
    })

@api_view(['POST'])
def send_otp(request):
    user_id = request.POST.get("user_id")
    otp = random.randint(1000,9999)

    user = User.objects.get(id = int(user_id))

    user_profile = UserProfile.objects.get(user = user)

    user_profile.otp = otp
    user_profile.save()

    URL = "http://sms.codicians.in/api/sendhttp.php?authkey=7322A5kha4jntu5ff1a099P6&mobiles={0}&message={1}&sender=BHROFF&route=4&country=91&response=json".format(user_profile.mobile_number,"Welcome {0}, your OTP for bharatoff account is {1}".format(user.username, user_profile.otp))

    import requests

    response = requests.get(URL)

    return Response({
        "message" : "success",
        "text" : "OTP sent successfully"
    })

@api_view(['POST'])
def varify_otp(request):
    user_id = request.POST.get("user_id")
    otp = request.POST.get("otp")

    if int(otp) == UserProfile.objects.get(user = User.objects.get(id = int(user_id))).otp:
        user_profile = UserProfile.objects.get(user = User.objects.get(id = int(user_id)))
        user_profile.is_varified = True
        user_profile.save()
        return Response({
            "message" : "success",
            "text" : "Account varified."
        })

@api_view(['POST'])
def category_wise_ad(request):
    schedule_refresh()
    cat_id = request.POST.get('cat_id')
    lat = request.POST.get('lat')
    lon = request.POST.get('lon')

    user = User.objects.get(id = int(request.POST.get("user_id")))
    
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
    
    category = Category.objects.get(id = int(cat_id))
    all_offers = Files.objects.all().filter(city = nearest_location.main_city, category = category, active=True)

    for i in range(len(all_offers)):
        if all_offers[i].active_image == 0:
            all_offers[i].real_image = all_offers[i].img
        elif all_offers[i].active_image == 1:
            all_offers[i].real_image = all_offers[i].img1
        elif all_offers[i].active_image == 2:
            all_offers[i].real_image = all_offers[i].img2
        elif all_offers[i].active_image == 3:
            all_offers[i].real_image = all_offers[i].img3
        elif all_offers[i].active_image == 4:
            all_offers[i].real_image = all_offers[i].img4
        elif all_offers[i].active_image == 5:
            all_offers[i].real_image = all_offers[i].img5
        elif all_offers[i].active_image == 6:
            all_offers[i].real_image = all_offers[i].img6
        elif all_offers[i].active_image == 7:
            all_offers[i].real_image = all_offers[i].img7
        elif all_offers[i].active_image == 8:
            all_offers[i].real_image = all_offers[i].img8
        elif all_offers[i].active_image == 9:
            all_offers[i].real_image = all_offers[i].img9
        
    context = {
        "message" : "success",
        "data" : []
    }

    coupon_history = CouponHistory.objects.all().filter(user=user)

    for data in all_offers:
        current_ad = {}
        current_ad["id"] = data.id
        current_ad["company_name"] = data.company_name
        current_ad["heading"] = data.heading
        current_ad["phone_number"] = data.phone_number
        current_ad["whatsapp_link"] = data.whatsapp_link
        current_ad["google_location"] = data.location
        current_ad["facebook_link"] = data.facebook_link
        current_ad["instagram_link"] = data.instagram_link
        current_ad["youtube_link"] = data.youtube_link
        current_ad["image_link"] = str(data.real_image)
        current_ad["rating"] = str(data.rating)

        current_ad["coupons"] = []

        all_coupons = Coupon.objects.all().filter(offer=data)

        for coupon in all_coupons:
            new_coupon_detail = {}
            new_coupon_detail["coupon_id"] = coupon.id
            new_coupon_detail["coupon_code"] = coupon.code
            new_coupon_detail["minimum_purchase"] = coupon.minimum_purchase
            new_coupon_detail["total_discount"] = coupon.total_discount
            new_coupon_detail["is_active"] = coupon.active
            new_coupon_detail["last_date"] = coupon.end_date

            # check the coupon status weather it is scratched or not

            is_scratched = False
            scratch_status = "NA"

            for history in coupon_history:
                if history.coupon.id == coupon.id:
                    is_scratched = True

                    if history.status:
                        scratch_status = "WINNER"
                    else:
                        scratch_status = "NOT_A_WINNER"
            
            new_coupon_detail["is_scratched"] = is_scratched
            new_coupon_detail["scratch_status"] = scratch_status

            current_ad["coupons"].append(new_coupon_detail)
        
        context["data"].append(current_ad)
    return Response(context)

@api_view(['POST'])
def create_user_with_phone_number(request):
    """
    This view will get a phone number, and a user will be generated as per CustomerLogin model,
    and the OTP will be send to the phone number mentioned. The API will return the message that OTP has been sent.
    """
    phone_number = request.POST.get("phone_number")

    if not phone_number:
        return Response({"message" : "Phone number not provided"})
    
    if len(phone_number) != 10:
        return Response({"message" : "Please recheck the phone number"})
    
    username = phone_number
    password = "".join(random.choices(string.ascii_uppercase, k=8))
    otp = random.randint(1000,9999)

    if not User.objects.all().filter(username=phone_number): # if user does not exist
        user = User.objects.create_user(username=phone_number, password=password)
        user.save()

        customer_profile = CustomerLogin.objects.create(user=user, otp=otp, is_varified=False, mobile=phone_number, password=password)
        customer_profile.coupon_code = "BOFF"+str(len(User.objects.all()))
        customer_profile.save()
    else: # if user with that phone number exist
        user = User.objects.get(username=phone_number)
        customer_profile = CustomerLogin.objects.get(user=user)
        customer_profile.otp = otp
        customer_profile.save()
    
    URL = "http://sms.codicians.in/api/sendhttp.php?authkey=7322A5kha4jntu5ff1a099P6&mobiles={0}&message={1}&sender=BHROFF&route=4&country=91&response=json".format(customer_profile.mobile,"Welcome {0}, your OTP for bharatoff account is {1}".format(customer_profile.mobile, customer_profile.otp))
    
    import requests
    response = requests.get(URL)

    print(response)
    print(response.text)

    return Response({"message":"SUCCESS"})

@api_view(['POST'])
def verify_otp(request):
    """
    INPUT: phone_number and otp
    OUTPUT: user_id

    This API will verify otp with the phone number
    """
    phone_number = request.POST.get('phone_number')
    otp = request.POST.get('otp')

    if not phone_number:
        return Response({"message" : "Phone number not provided"})
    if not otp:
        return Response({"message" : "OTP not provided"})
    
    if len(phone_number) != 10:
        return Response({"message" : "Please recheck the phone number"})

    customer_profile = CustomerLogin.objects.get(user = User.objects.get(username=phone_number))
    
    if int(customer_profile.otp) == int(otp):
        customer_profile.is_varified = True
        customer_profile.save()
        return Response({
            "message" : "SUCCESS",
            "user_id" : User.objects.get(username=phone_number).id,
            "email" : User.objects.get(username=phone_number).email
        })
    else:
        user = User.objects.get(username=phone_number)
        # user.delete()
        return Response({
            "message" : "OTP mismatched"
        })

@api_view(['POST'])
def scratch_coupon(request):
    schedule_refresh()
    
    context = {}
    
    user_id = int(request.POST.get('user_id'))
    coupon_id = int(request.POST.get('coupon_id'))

    user = User.objects.get(id=user_id)
    coupon = Coupon.objects.get(id=coupon_id)

    history = CouponHistory.objects.all().filter(user=user, coupon=coupon)

    if history:
        if history[0].status:
            return Response({
                "message" : "SUCCESS",
                "data" : {
                    "note" : "Already Scratched",
                    "status" : True,
                    "coupon_info" : {
                        "code" : coupon.code,
                        "expiry_date" : coupon.end_date,
                        "active" : coupon.active,
                        "minimum_purchase" : coupon.minimum_purchase,
                        "total_discount" : coupon.total_discount,
                        "is_redeemed" : history[0].is_redeemed,
                    }
                }
            })
        else:
            return Response({
                "message" : "SUCCESS",
                "data" : {
                    "note" : "Already Scratched",
                    "status" : False
                }
            })
    else:
        if random.choice([True, False]):
            history_object = CouponHistory.objects.create(user=user, coupon=coupon, status=True)
            history_object.save()
            return Response({
                "message" : "SUCCESS",
                "data" : {
                    "note" : "WINNER",
                    "status" : True,
                    "coupon_info" : {
                        "code" : coupon.code,
                        "expiry_date" : coupon.end_date,
                        "active" : coupon.active,
                        "minimum_purchase" : coupon.minimum_purchase,
                        "total_discount" : coupon.total_discount,
                        "is_redeemed" : history_object.is_redeemed,
                    }
                }
            })
        else:
            history_object = CouponHistory.objects.create(user=user, coupon=coupon, status=False)
            history_object.save()
            return Response({
                "message" : "SUCCESS",
                "data" : {
                    "status" : False,
                    "note" : "Better luck next time"
                }
            })
    return Response(context)

@api_view(["POST"])
def make_coupon_redeemed(request):
    user_id = int(request.POST.get("user_id"))
    coupon_id = int(request.POST.get("coupon_id"))

    user = User.objects.get(id=user_id)
    coupon = Coupon.objects.get(id=coupon_id)

    coupon_history = CouponHistory.objects.get(user=user, coupon=coupon)

    coupon_history.is_redeemed = True
    coupon_history.save()

    return Response({
        "message" : "SUCCESS",
        "data" : {
            "user_id" : user_id,
            "coupon_id" : coupon_id,
            "note" : "Coupon Redeemed"
        }
    })


@api_view(["POST"])
def log_payment_issue(request):
    user_id = int(request.POST.get("user_id"))
    coupon_id = int(request.POST.get("coupon_id"))
    message = request.POST.get("message")

    user = User.objects.get(id=user_id)
    coupon = Coupon.objects.get(id=coupon_id)

    payment_issue = PaymentIssue.objects.create(user=user, coupon=coupon, offer = coupon.offer, message=message)
    payment_issue.save()

    return Response({
        "message" : "SUCCESS",
        "data" : {
            "payment_issue_id" : payment_issue.id,
            "message" : payment_issue.message
        }
    })
    pass


@api_view(["POST"])
def get_coupon_history(request):
    user_id = int(request.POST.get('user_id'))

    history = CouponHistory.objects.all().filter(user = User.objects.get(id=user_id), status=True)

    context = {
        "message" : "SUCCESS",
        "data" : []
    }

    for data in history:
        if data.status:
            context["data"].append(
                {
                    "coupon_id" : data.coupon.id,
                    "coupon_code" : data.coupon.code,
                    "expiry_date" : data.coupon.end_date,
                    "minimum_purchase" : data.coupon.minimum_purchase,
                    "total_discount" : data.coupon.total_discount,
                    "shop_name" : data.coupon.offer.company_name,
                    "shop_id" : data.coupon.offer.id,
                    "is_redeemed" : data.is_redeemed
                }
            )
    
    return Response(context)

@api_view(["POST"])
def update_profile(request):
    user_id = int(request.POST.get('user_id'))
    new_email = request.POST.get('new_email')
    
    if not user_id:
        return Response({
            "message" : "FAILURE",
            "data" : "user_id not provided"
        })
    
    if not new_email:
        return Response({
            "message" : "FAILURE",
            "data" : "new_email not provided"
        })

    user_object = User.objects.get(id = user_id)
    user_object.email = request.POST.get('new_email')
    user_object.save()

    return Response({
        "message" : "SUCCESS",
        "data" : "Email changed successfully."
    })

@api_view(["POST"])
def update_user_location(request):
    user_id = int(request.POST.get('user_id'))

    user = User.objects.get(id=user_id)
    latitude = request.POST.get("lat")
    longitude = request.POST.get("lon")

    try:
        customer_profile = CustomerLogin.objects.get(user=user)
        customer_profile.latitude = latitude
        customer_profile.longitude = longitude
        customer_profile.save()
    except:
        customer_profile = CustomerLogin.objects.create(user=user, password="Linux@123")
        customer_profile.latitude = latitude
        customer_profile.longitude = longitude
        customer_profile.save()


    return Response({
        "message" : "SUCCESS",
        "data" : {
            "user_id" : user_id,
            "latitude" : customer_profile.latitude,
            "longitude" : customer_profile.longitude
        }
    })

@api_view(["POST"])
def get_notification(request):
    user_id = int(request.POST.get('user_id'))

    user = User.objects.get(id=user_id)

    user_notifications = UserNotification.objects.all().filter(target_user=user).order_by("-timestamp")

    notifications = []

    for notification in user_notifications:
        notifications.append({
            "notification_text" : notification.notification_text,
            "timestamp" : notification.timestamp
        })
    
    return Response({
        "message" : "SUCCESS",
        "data" : {
            "all_notifications" : notifications
        }
    })

@api_view(["POST"])
def enroll_device_id(request):

    user_id = int(request.POST.get("user_id"))
    device_id = request.POST.get("device_id")

    user = User.objects.get(id=user_id)

    new_device = DeviceID.objects.create(user=user, device_id = device_id)
    new_device.save()
    
    return Response({
        "message" : "SUCCESS",
        "date" : {
            "user_id" : user_id,
            "device_id" : device_id
        }
    })

@api_view(["POST"])
def send_enquiry_alert(request):
    user_id = request.POST.get("user_id")
    shop_id = request.POST.get("shop_id")

    user = User.objects.all().filter(id = int(user_id))[0]
    shop = Files.objects.all().filter(id = shop_id)[0]
    
    shopkeeper_name = request.POST.get('shopkeeper_name')
    shopkeeper_phone_number = request.POST.get('shopkeeper_phone_number')
    customer_phone_number = request.POST.get('customer_phone_number')

    sms_delivery.send_enquiry_text(shopkeeper_name, shopkeeper_phone_number, customer_phone_number)

    enquiry_log = EnquiryLog.objects.create(user = user, shop=shop)
    enquiry_log.save()

    return Response({
        "message" : "SUCCESS"
    })

@api_view(["POST"])
def check_if_eligible_for_today(request):
    user_id = request.POST.get("user_id")
    shop_id = request.POST.get("shop_id")

    user = User.objects.all().filter(id = int(user_id))[0]
    shop = Files.objects.all().filter(id = shop_id)[0]

    today = datetime.today()

    enquiry_log = EnquiryLog.objects.all().filter(user = user, shop = shop, date = today)[0]

    if enquiry_log:
        return Response({
            "message" : "SUCCESS",
            "data" : {
                "user_id" : user_id,
                "shop_id" : shop_id,
                "status_code" : 0,
                "status_log" : "NOT_ELIGIBLE"
            }
        })
    else:
        return Response({
            "message" : "SUCCESS",
            "data" : {
                "user_id" : user_id,
                "shop_id" : shop_id,
                "status_code" : 1,
                "status_log" : "ELIGIBLE"
            }
        })