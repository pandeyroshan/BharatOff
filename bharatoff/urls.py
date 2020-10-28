from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as users_views
from management import views as management_views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', users_views.register, name='register'),
    path('register-shop/', users_views.register_shopkeepers, name='register-shop'),
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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)