from django.urls import path, include
import recipe.views as views
from rest_framework.routers import DefaultRouter



urlpatterns = [

    # 这里需要末尾的 /
    path("systemrecipe/", views.SystemRecipeViewSet.as_view(
        {'get': 'brief_list'}
        )),
    path("systemrecipe/<int:pk>", views.SystemRecipeViewSet.as_view(
        {'get': 'detailed_retrieve'}
        )),
    path("orderrecipe/<int:pk>", views.OrderRecipeViewSet.as_view(
        {'get': 'list'}
        )),
    path("productrecipe/<int:pk>", views.ProductRecipeViewSet.as_view(
        {'get': 'retrieve'}
        )),
]