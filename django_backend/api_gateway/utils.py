from .models import Tenant
from rest_framework.exceptions import AuthenticationFailed

class TenantContextMixin:
    def get_tenant(self, request):
        tenant_id = request.auth.get('tenant_id')
        try:
            return Tenant.objects.get(id=tenant_id)
        except Tenant.DoesNotExist:
            raise AuthenticationFailed("Invalid Tenant. Token does not match any tenant.")
