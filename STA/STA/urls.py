from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # DRF 的登录和退出
    path("material_category/", include("material_category.urls")),
]