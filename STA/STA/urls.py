from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# drf_yasg2 配置
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
 



urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'), # drf_yasg2 配置
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # drf_yasg2 配置
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # drf_yasg2 配置
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # DRF 的登录和退出
    path("material_category/", include("material_category.urls")),
    path("order/", include("order.urls")),
    path("product/", include("product.urls")),
    path("recipe/", include("recipe.urls")),
    path("sta_auth/", include("sta_auth.urls")),
    path("consume/", include("consume.urls")),
]


 
