from django.contrib import admin
from .models import CustomerInfo,CustomerEnquiry
class CinfoAdmin(admin.ModelAdmin):
    list_display=("name","contact","email","social_media","feedback","purchased_item","gender")
admin.site.register(CustomerInfo,CinfoAdmin)
class CenqAdmin(admin.ModelAdmin):
    list_display=("name","time","enquiry")
admin.site.register(CustomerEnquiry,CenqAdmin)
 
