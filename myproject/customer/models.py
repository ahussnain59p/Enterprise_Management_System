from django.db import models
# HR RESOURCES
class CustomerInfo(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField(blank=True, default='')
    email=models.CharField(max_length=50,blank=True, default='')
    social_media=models.CharField(max_length=30,blank=True, default='')
    feedback=models.TextField(max_length=300,blank=True, default='')
    purchased_item=models.TextField()
    gender=models.TextField(blank=True, default='')
    
class CustomerEnquiry(models.Model):
    name=models.CharField(max_length=50)
    time=models.DateField()
    enquiry=models.TextField()