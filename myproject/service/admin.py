from django.contrib import admin
from service.models import Service,Signup,Signin
class ServiceAdmin(admin.ModelAdmin):
    list_display=("service_icon","service_title","service_des")
admin.site.register(Service,ServiceAdmin)
class SignUp(admin.ModelAdmin):
    list_display=("username","email","password")
admin.site.register(Signup,SignUp)
