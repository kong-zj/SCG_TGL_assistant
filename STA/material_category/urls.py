from django.urls import path, include
import material_category.views as views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix="category", viewset=views.CategoryViewSet)


urlpatterns = [
    path("hello_world", views.hello_world),
    # CBV
    path("cbv/list", views.CourseList.as_view(), name="cbv-list"),
    # 自动绑定
    path("", include(router.urls)),
]