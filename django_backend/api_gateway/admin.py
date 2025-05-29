from django.contrib import admin

# Register your models here.

from .models import Tenant, CompanyCategory

@admin.register(Tenant)

class TenantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "short_instructions")
    list_filter = ("category",)
    search_fields = ("id", "name")
    fields = ("category", "instructions")

    def short_instructions(self, obj):
        return (obj.instructions[:60]+"...") if obj.instructions and len(obj.instructions) > 60 else (obj.instructions or "")
    short_instructions.short_description = "Instructions (preview)"

    
@admin.register(CompanyCategory)
class CompanyCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "short_instructions")
    search_fields = ("name",)
    fields = ("name", "description", "instructions", "created_at")
    readonly_fields = ("created_at",)

    def short_instructions(self, obj):
        return (obj.instructions[:60] + '...') if len(obj.instructions) > 60 else obj.instructions
    short_instructions.short_description = "Instructions (preview)"
