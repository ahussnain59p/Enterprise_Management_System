from django.contrib import admin
from .models import EmployeeInfo,ManufactureInfo,SaleInfo
class EmployeeAdmin(admin.ModelAdmin):
    list_display=("name","age","department","payroll","performance_eval","bonus","joining_date","training_duration_months")
admin.site.register(EmployeeInfo,EmployeeAdmin)
class ManufactureAdmin(admin.ModelAdmin):
    list_display=("product_name","quantity","quality_control","starting_date","expected_finishing_date")
admin.site.register(ManufactureInfo,ManufactureAdmin)
class SaleAdmin(admin.ModelAdmin):
    list_display=("product_name","price","quality","buyer_name","purchasing_date")
admin.site.register(SaleInfo,SaleAdmin)
