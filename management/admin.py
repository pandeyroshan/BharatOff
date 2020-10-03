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
    WebCounter
)


admin.site.site_header = "Bharatoff Administration"


class MiniLocationInline(admin.TabularInline):
    model = MiniLocation
    extra = 1


class CityAdmin(admin.ModelAdmin):
    inlines = [MiniLocationInline,]
    model = CityData
    list_display = ('city_name','lat','lon')


class VisitorAdmin(admin.ModelAdmin):
    model = Visitors
    readonly_fields = ('counter',)


admin.site.register(CityData,CityAdmin)
admin.site.register(Files)

# admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(StateData)
admin.site.register(Address)
admin.site.register(Visitors,VisitorAdmin)
admin.site.register(VisitCount)
admin.site.register(Messages)
admin.site.register(Category)
admin.site.register(WebCounter)