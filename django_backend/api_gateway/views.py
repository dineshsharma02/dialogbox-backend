from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenPairObtainSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Tenant
from .utils import TenantContextMixin


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenPairObtainSerializer


class HelloWorldView(TenantContextMixin,APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant = self.get_tenant(request)
        return Response({
            "message": f"Hello, {tenant.name}",
            "tenant_id": tenant.id
        })