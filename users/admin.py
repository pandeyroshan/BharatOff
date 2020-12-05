from django.contrib import admin

# Register your models here.
from .models import UserProfile,Shopkeeper, Freelancer

class ShopkeeperAdmin(admin.ModelAdmin):
    model = Shopkeeper
    list_display = ('user','mobile_number','pwd','city')
    search_fields = ('user',)
    list_filter = ('city',)
    readonly_fields = ('user','pwd')

class FreelancerAdmin(admin.ModelAdmin):
    model = Freelancer
    list_display = ('user', 'mobile_number', 'pwd', 'comes_under')
    radio_fields = {"comes_under": admin.HORIZONTAL}
    readonly_fields = ('user','pwd')

admin.site.register(UserProfile)
admin.site.register(Shopkeeper, ShopkeeperAdmin)
admin.site.register(Freelancer, FreelancerAdmin)