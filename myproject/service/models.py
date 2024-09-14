from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
class Service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=90)
    service_des=models.TextField()
class Signup(models.Model):
    username = models.CharField(max_length=90)
    email = models.EmailField(max_length=90, unique=True)
    password = models.CharField(max_length=95, validators=[
        RegexValidator(
            regex=r'^.*[a-z].*$',
            message='Password must contain at least one lowercase letter.',
        ),
        RegexValidator(
            regex=r'^.*[A-Z].*$',
            message='Password must contain at least one uppercase letter.',
        ),
        RegexValidator(
            regex=r'^.*[\W_].*$',
            message='Password must contain at least one special character.',
        ),
    ])
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.username
class Signin(models.Model):
    email = models.EmailField(max_length=90)
    password = models.CharField(max_length=90)
    def __str__(self):
        return self