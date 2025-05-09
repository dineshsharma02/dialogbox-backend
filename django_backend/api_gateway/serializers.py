from rest_framework import serializers
from .models import Tenant
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"


class MyTokenPairObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        try:
            token["tenant_id"] = user.tenant.id
        except:
            token["tenant_id"] = None
        
        return token
    


class UserQuerySerializer(serializers.Serializer):
    question = serializers.CharField(max_length = 1000)