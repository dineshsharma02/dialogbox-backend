from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView, UserQueryView
from django.urls import path
urlpatterns = [
    path("api/token/", MyTokenObtainPairView.as_view(), name = "token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name = "token_refresh"),
    path("user/query", UserQueryView.as_view(),name = "user_query"),
]
