from django.urls import path, include
import material_category.views as views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 这里不需要末尾的 /
router.register(prefix="category", viewset=views.CategoryViewSet)
router.register(prefix="material_link_category", viewset=views.MaterialLinkCategoryViewSet)


urlpatterns = [
    # DRF CBV
    # 这里需要末尾的 /
    path("material/", views.OriginalMaterialViewSet.as_view(
        {'get': 'list'}
        )),
    path("material/<int:pk>", views.OriginalMaterialViewSet.as_view(
        {'get': 'retrieve'}
        )),
    # 自动绑定
    path("", include(router.urls)),
]