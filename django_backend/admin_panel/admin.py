from django.contrib import admin

# Register your models here.
from .models import FAQ 


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question","tenant__name","created_at")
    list_filter = ("tenant",)
    search_fields = ("question", "answer")