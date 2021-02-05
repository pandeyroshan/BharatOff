from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as users_views
from management import views as management_views
from . import settings
from django.conf.urls.static import static
from management import api_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', users_views.register, name='register'),
    path('register-shop/', users_views.register_shopkeepers, name='register-shop'),
    path('register-freelancer/', users_views.register_freelancer, name='register-freelancer'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),    

    path('', management_views.home,name='home'),
    path('location', management_views.location_based, name='location-based'),
    path('city/<int:id>/', management_views.city_ad, name='city_add'),
    path('minilocations/<int:id>/', management_views.minilocations, name='minilocations'),
    path('location/broad/<int:id>/', management_views.single, name='single'),
    path('contact/', management_views.contact, name='contact'),
    path('search/', management_views.search, name='search'),

    path('dashboard/', management_views.dashboard, name='dashboard'),

    path('category/fashion/<int:id>/', management_views.fashion, name='fashion'),
    path('category/property/<int:id>/', management_views.property, name='property'),
    path('category/electronics/<int:id>/', management_views.MobileElectronic, name='electronic'),
    path('category/food/<int:id>/', management_views.RestBakery, name='food'),
    path('category/supermarket/<int:id>/', management_views.supermarket, name='supermarket'),
    path('category/service/<int:id>/', management_views.service, name='service'),

    path('category/<int:cid>/<int:mlid>/', management_views.category, name='category'),
    path('settings/<int:id>/', management_views.ad_setting, name='setting'),

    path('access/abort/',management_views.abort_admin_access, name='abort'),
    path('access/allow/',management_views.allow_admin_access, name='allow'),

    path('refresh/',management_views.refresh_ads, name='refresh'),
    path('image/', management_views.image_resource, name='resources'),
    path('download/<int:id>/',management_views.download_image, name='download'),

    path('save-coupon/', management_views.save_coupon, name='save-coupon'),

    # api work goes here 

    path('api/all-categories/',api_views.all_categories),
    path('api/category/',api_views.category_wise_ad),
    path('api/all-advertisement/', api_views.all_advertisement),
    path('api/all-states/',api_views.get_all_states),
    path('api/all-cities/',api_views.get_cities),
    path('api/all-minilocations/',api_views.get_minilocation),
    path('api/individual-ad/',api_views.get_ad_detail),
    path('api/search/',api_views.get_search_result),
    path('api/rating/',api_views.rate_ad),  # takes ad_id and rating 
    path('api/register/', api_views.create_user_with_phone_number), # creates user and sends OTP with given phone number
    path('api/verify-otp/',api_views.verify_otp), # pass phone number and otp (that user entered)
    path('api/scratch/',api_views.scratch_coupon),
    path('api/coupon-history/',api_views.get_coupon_history),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)