from django.contrib import admin
from django.contrib.auth.models import User,Group
from management.models import (
    CityData,
    Files,
    StateData,
    Address,
    Visitors,
    VisitCount,
    Messages,
    MiniLocation,
    Category,
    WebCounter,
    MarketingSources,
    PackageType,
    Resources,
    Coupon,
    CouponHistory,
)

admin.site.site_header = "Bharatoff Administration"


class MiniLocationInline(admin.TabularInline):
    model = MiniLocation
    extra = 1


class CityAdmin(admin.ModelAdmin):
    inlines = [MiniLocationInline,]
    model = CityData
    list_display = ('city_name','lat','lon')
    search_fields = ('city_name',)


class VisitorAdmin(admin.ModelAdmin):
    model = Visitors
    readonly_fields = ('counter',)

class FilesAdmin(admin.ModelAdmin):
    model = Files
    list_display = ('company_name','package_type','user','heading','category','date','activated_till','rating','active')
    search_fields = ('company_name',)
    list_filter = ('active',)
    radio_fields = {"category": admin.HORIZONTAL,"user" : admin.HORIZONTAL}
    filter_horizontal = ['city','MiniLocation']
    # exclude = ('counter',)

class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ('address','mail','phone_number',)

    def has_add_permission(self, request):
        return True
    
    def has_delete_permission(self,request,obj=None):
        return True

class MessageAdmin(admin.ModelAdmin):
    model = Messages
    list_display = ('name','email','subject')

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

class StateAdmin(admin.ModelAdmin):
    model = StateData
    search_fields = ('state_name',)

class MarketingSourcesAdmin(admin.ModelAdmin):
    model = MarketingSources
    list_display = ('source','counter')
    search_fields = ('source',)

class PackageTypeAdmin(admin.ModelAdmin):
    model = PackageType
    list_display = ('name','price','total_phamplet','total_videos')
    search_fields = ('name',)

class CouponAdmin(admin.ModelAdmin):
    model = Coupon
    list_display = ('user','code','offer','start_date','end_date','total_coupon','active')
    search_fields = ('code',)

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj = None):
        return False
    
    def has_change_permission(self, request, obj = None):
        return False

class CouponHistoryAdmin(admin.ModelAdmin):
    model = CouponHistory
    list_display = ('code','user','status','expiry_date')

    def has_add_permission(self, request):
        return True
    
    def has_delete_permission(self, request, obj = None):
        return True
    
    def has_change_permission(self, request, obj = None):
        return True

admin.site.register(CityData,CityAdmin)
admin.site.register(Files,FilesAdmin)

# admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(StateData, StateAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Visitors, VisitorAdmin)
admin.site.register(Category)
admin.site.register(WebCounter)
admin.site.register(Messages, MessageAdmin)
admin.site.register(MarketingSources, MarketingSourcesAdmin)
admin.site.register(PackageType, PackageTypeAdmin)
admin.site.register(Resources)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(CouponHistory, CouponHistoryAdmin)