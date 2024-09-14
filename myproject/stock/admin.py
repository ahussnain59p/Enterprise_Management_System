from django.contrib import admin
from .models import FinishedProduct,RawMaterial
class FinishedProdAdmin(admin.ModelAdmin):
    list_display=("name","quantity","placed_section","price","finishing_date","stocked_time")
admin.site.register(FinishedProduct,FinishedProdAdmin)
class RawmatAdmin(admin.ModelAdmin):
    list_display=("name","quantity","placed_section","price","delivery_date","stocked_time")
admin.site.register(RawMaterial,RawmatAdmin)

