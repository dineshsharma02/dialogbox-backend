
from django.urls import path
from .views import upload_faq_view

urlpatterns = [
    path("upload-faqs/", upload_faq_view, name="upload-faqs"),
]
