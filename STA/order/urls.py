from django.urls import path, include
import order.views as views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    # DRF CBV
    # 这里需要末尾的 /
    path("order/", views.OrderViewSet.as_view(
        {'get': 'list'}
        )),
    path("order/<int:pk>", views.OrderViewSet.as_view(
        {'get': 'retrieve'}
        )),
]