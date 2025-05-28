from django.contrib import admin

# Register your models here.

from .models import Tenant, CompanyCategory

@admin.register(Tenant)

class TenantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("id", "name")
    fields = (..., "category", "instructions")

    
@admin.register(CompanyCategory)
class CompanyCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
