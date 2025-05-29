from django.db import models
from django.contrib.auth.models import User



    
class CompanyCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank = True)
    instructions = models.TextField(
        help_text="LLM system prompt for this company category (shown in chatbot prompt)."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
# Create your models here.
class Tenant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255) # client company's name
    api_key = models.CharField(max_length=255, unique = True) # To verify the company 
    category = models.ForeignKey(CompanyCategory, on_delete=models.SET_NULL, null = True, blank = True, related_name="tenants")
    created_at = models.DateTimeField(auto_now_add = True) #audit/logging purpose
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    instructions = models.TextField(
        blank=True,
        help_text="(Optional) Custom LLM prompt instructions for this tenant. If blank, falls back to category instructions."
    )



