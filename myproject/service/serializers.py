from rest_framework import serializers
from .models import Service,Signup
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "id","service_icon","service_title","service_des"
class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = "id","username","email","password"