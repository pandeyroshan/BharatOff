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
    MarketingSources
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
    list_display = ('company_name','user','heading','category','date','activated_till','active')
    search_fields = ('company_name',)
    list_filter = ('active',)

class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ('address','mail','phone_number',)

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self,request,obj=None):
        return False

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

admin.site.register(CityData,CityAdmin)
admin.site.register(Files,FilesAdmin)

# admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(StateData,StateAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Visitors,VisitorAdmin)
admin.site.register(Category)
admin.site.register(WebCounter)
admin.site.register(Messages,MessageAdmin)
admin.site.register(MarketingSources,MarketingSourcesAdmin)