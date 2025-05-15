from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenPairObtainSerializer, UserQuerySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Tenant
from .utils import TenantContextMixin
from rest_framework.response import Response
from .user_query_pipeline import process_user_query
import time


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
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        start_time = time.time()
        serializer = UserQuerySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        tenant = self.get_tenant(request)
        question = serializer.validated_data['question']
        result = process_user_query(question, tenant.id)
        end_time = time.time()
        latency_ms = round((end_time - start_time) * 1000, 2)

        return Response({
            "success": True,
            "latency":latency_ms,
            "data": {
                "query": result["query"],
                "matched_answers": result["context_used"],
                "final_answer": result["answer"]
            }
        })