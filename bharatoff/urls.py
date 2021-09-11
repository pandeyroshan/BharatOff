from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as users_views
from management import views as management_views
from . import settings
from django.conf.urls.static import static
from management import api_views
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', users_views.register, name='register'),
    path('register-shop/', users_views.register_shopkeepers, name='register-shop'),
    path('register-freelancer/', users_views.register_freelancer, name='register-freelancer'),
    # path('register-sales/', users_views.register_sales, name='register-sales'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='users/change-password.html',success_url='/'),name='change-password'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('update-password/', users_views.update_password, name="update-password"),
    path('forgot-password/', users_views.forgot_password, name="forgot-password"),

    path('shop-registration/', management_views.register_shopkeeper, name="register-shop"),  
    path('view-shop-details/', management_views.view_shop_details, name="view-shop-details"),
    path('view-shop-details-freelancer/', management_views.view_shop_details_freelancer, name="view-shop-details-freelancer"),
    path('forward-to-freelancer/', management_views.forward_to_freelancer, name="forward-to-freelancer"),
    path('approve-design/', management_views.approve_design, name="approve-design"),
    path('reject-design', management_views.reject_with_comment, name="reject-design"),
    path('upload-design', management_views.upload_design, name="upload-design"),
    path('success/', management_views.shop_registration_successful, name="register-shop-success"),  
    path('update-social-links', management_views.update_social_media_links, name="update-social-media"),
    path('', management_views.home,name='home'),
    path('location', management_views.location_based, name='location-based'),
    path('city/<int:id>/', management_views.city_ad, name='city_add'),
    path('minilocations/<int:id>/', management_views.minilocations, name='minilocations'),
    path('location/broad/<int:id>/', management_views.single, name='single'),
    path('contact/', management_views.contact, name='contact'),
    path('search/', management_views.search, name='search'),

    path('dashboard/', management_views.dashboard, name='dashboard'),
    path('freelancer/', management_views.freelancer_dashboard, name="freelancer-dashboard"),

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

    # sales dashboard 

    path('sales/', management_views.sales_dashboard, name='sales-dashboard'),
    path('security-report/<int:id>', management_views.raise_security_concern, name='raise-security-concern'),

    # notification work goes down here 
    path("create-notification-alert", users_views.create_notification_alert, name="create-notification-alert"),

    # mothly rewards
    path("rewards/", users_views.rewards_homepage, name="rewards-homepage"),
    path("allocate-winners", users_views.find_winners, name="allocate-winners"),

    # image editing work
    path("test/", management_views.image_editing, name="image-editing"),

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
    path('api/redeem/', api_views.make_coupon_redeemed),  # pass coupon_id and user_id to redeem a coupon 
    path("api/report-coupon/", api_views.log_payment_issue),
    path('api/update-profile/', api_views.update_profile),
    path('api/update-user-location/', api_views.update_user_location),
    path('api/get-notification', api_views.get_notification),
    path('api/enroll-device-id/', api_views.enroll_device_id),


    # path('invoice/<str:invoice_id>', management_views.show_pdf, name='show-invoice'),
    path('invoice/', management_views.show_pdf, name='show-invoice'),
    path('invoices/', management_views.show_all_invoices, name='download-all-invoice'),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)