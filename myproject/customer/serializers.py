from rest_framework import serializers
from .models import CustomerInfo,CustomerEnquiry
class CinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = "id","name","contact","email","social_media","feedback","purchased_item","gender"
class CenqSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerEnquiry
        fields = "id","name","time","enquiry"