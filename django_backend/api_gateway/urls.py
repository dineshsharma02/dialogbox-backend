from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView
from django.urls import path
from .views import HelloWorldView

urlpatterns = [
    path("api/token/", MyTokenObtainPairView.as_view(), name = "token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name = "token_refresh"),
    path("api/hello", HelloWorldView.as_view(), name = "hello_view")


]
