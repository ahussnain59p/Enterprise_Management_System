from rest_framework import serializers
from .models import FinishedProduct,RawMaterial
class FinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinishedProduct
        fields = "id","name","quantity","placed_section","price","finishing_date","stocked_time"
class RawmatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = "id","name","quantity","placed_section","price","delivery_date","stocked_time"