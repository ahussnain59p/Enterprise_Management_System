from rest_framework import serializers
from .models import EmployeeInfo,ManufactureInfo,SaleInfo
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = "id","name","age","department","payroll","performance_eval","bonus","joining_date","training_duration_months"
class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufactureInfo
        fields = "id","product_name","quantity","quality_control","starting_date","expected_finishing_date"
class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleInfo
        fields = "id","product_name","price","quality","buyer_name","purchasing_date"