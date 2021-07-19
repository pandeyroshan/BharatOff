from django.contrib import admin

# Register your models here.
from .models import UserProfile,Shopkeeper, Freelancer, CustomerLogin, SalesPerson

class ShopkeeperAdmin(admin.ModelAdmin):
    model = Shopkeeper
    list_display = ('user','mobile_number','pwd','city')
    search_fields = ('user',)
    list_filter = ('city',)
    readonly_fields = ('user','pwd')
    exclude = ('otp',)

class FreelancerAdmin(admin.ModelAdmin):
    model = Freelancer
    list_display = ('user', 'mobile_number', 'pwd', 'comes_under')
    radio_fields = {"comes_under": admin.HORIZONTAL}
    readonly_fields = ('user','pwd')

class CustomerLoginAdmin(admin.ModelAdmin):
    model = CustomerLogin
    list_display = ('user', 'password', 'mobile', 'otp', 'is_varified')

class SalesPersonAdmin(admin.ModelAdmin):
    model = SalesPerson
    readonly_fields = ('user', 'pwd')
    exclude = ('otp',)
    list_display = ('user','city')

admin.site.register(UserProfile)
admin.site.register(Shopkeeper, ShopkeeperAdmin)
admin.site.register(Freelancer, FreelancerAdmin)
admin.site.register(CustomerLogin, CustomerLoginAdmin)
admin.site.register(SalesPerson, SalesPersonAdmin)