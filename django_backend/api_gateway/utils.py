from .models import Tenant
from rest_framework.exceptions import AuthenticationFailed

class TenantContextMixin:
    def get_tenant(self, request):
        tenant_id = request.auth.get('tenant_id') if request.auth else None
        tenant_id = tenant_id or request.GET.get("t")

        if not tenant_id:
            raise AuthenticationFailed("No tenant ID provided.")
        try:
            return Tenant.objects.get(id=tenant_id)
        except Tenant.DoesNotExist:
            raise AuthenticationFailed("Invalid Tenant. Token does not match any tenant.")
