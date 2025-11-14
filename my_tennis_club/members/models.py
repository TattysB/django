from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone=models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    email = models.EmailField(max_length=255, null=True)
    gender = models.CharField(max_length=100, null=True)
    registration_time = models.DateTimeField(auto_now_add=True, null=True)
    
    
    
    
