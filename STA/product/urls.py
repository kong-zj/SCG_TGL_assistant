from django.urls import path, include
import product.views as views
from rest_framework.routers import DefaultRouter



urlpatterns = [

    # 这里需要末尾的 /
    path("product/", views.ProductViewSet.as_view(
        {'get': 'list'}
        )),
    path("product/<int:pk>", views.ProductViewSet.as_view(
        {'get': 'retrieve'}
        )),
]