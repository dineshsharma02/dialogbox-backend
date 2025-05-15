from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView, UserQueryView
from django.urls import path
from .views import HelloWorldView, upload_faq_view

urlpatterns = [
    path("api/token/", MyTokenObtainPairView.as_view(), name = "token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name = "token_refresh"),
    path("api/hello", HelloWorldView.as_view(), name = "hello_view"),
    path("user/query", UserQueryView.as_view(),name = "user_query"),
    path("admin/upload-faqs/", upload_faq_view, name="upload-faqs"),


]
