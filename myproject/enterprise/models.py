from django.db import models
# HR RESOURCES
class EmployeeInfo(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    department=models.CharField(max_length=50)
    payroll=models.IntegerField()
    performance_eval=models.CharField(max_length=50)
    bonus=models.IntegerField()
    joining_date=models.DateField()
    training_duration_months=models.IntegerField()


class ManufactureInfo(models.Model):
    product_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    quality_control=models.TextField()
    starting_date=models.DateField()
    expected_finishing_date=models.DateField()


class SaleInfo(models.Model):
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()
    quality=models.TextField()
    buyer_name=models.CharField(max_length=50)
    purchasing_date=models.DateField()


