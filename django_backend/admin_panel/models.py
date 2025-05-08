from django.db import models
from api_gateway.models import Tenant

# Create your models here.


class FAQ(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    question = models.CharField(max_length=512)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tenant.name} - {self.question[:50]}"
