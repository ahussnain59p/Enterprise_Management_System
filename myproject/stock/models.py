from django.db import models
class FinishedProduct(models.Model):
    name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    placed_section=models.TextField()
    price=models.IntegerField()
    finishing_date=models.DateField()
    stocked_time=models.IntegerField()
class RawMaterial(models.Model):
    name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    placed_section=models.TextField()
    price=models.IntegerField()
    delivery_date=models.DateField()
    stocked_time=models.IntegerField()
