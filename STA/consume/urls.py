from django.urls import path, include
import consume.views as views
from rest_framework.routers import DefaultRouter



urlpatterns = [

    # 这里需要末尾的 /
    path("productdetailedconsume/<int:product_pk>", views.ProductConsumeViewSet.as_view(
        {'get': 'detailed_retrieve'}
        )),
    path("productbriefconsume/<int:product_pk>", views.ProductConsumeViewSet.as_view(
        {'get': 'brief_retrieve'}
        )),
]
