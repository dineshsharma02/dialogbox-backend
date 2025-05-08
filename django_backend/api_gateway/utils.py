from .models import Tenant

class TenantContextMixin:
    def get_tenant(self, request):
        tenant_id = request.auth.get('tenant_id')
        return Tenant.objects.get(id=tenant_id)
