from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tenant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255) # client company's name
    api_key = models.CharField(max_length=255, unique = True) # To verify the company 
    created_at = models.DateTimeField(auto_now_add = True) #audit/logging purpose
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)

    