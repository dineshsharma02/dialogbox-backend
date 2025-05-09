from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenPairObtainSerializer, UserQuerySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Tenant
from .utils import TenantContextMixin
from rest_framework.response import Response



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
    

class UserQueryView(TenantContextMixin, APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserQuerySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        tenant = self.get_tenant(request)
        question = serializer.validated_data['question']


        return Response({
            "tenant":tenant.name,
            "question":question,
            "answer":f"You asked: '{question} - I'll answer this soon.'"
        })