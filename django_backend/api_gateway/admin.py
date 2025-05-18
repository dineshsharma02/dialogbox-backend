from django.contrib import admin

# Register your models here.

from .models import Tenant

@admin.register(Tenant)

class TenantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("id", "name")

    