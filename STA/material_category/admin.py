from django.contrib import admin
from .models import Category, MaterialLinkCategory

# 在Django的admin后台中管理我们的数据
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryId', 'categoryName', 'intoStatisticsFlag')
    search_fields = list_display
    list_filter = list_display
    
@admin.register(MaterialLinkCategory)
class MaterialLinkCategoryAdmin(admin.ModelAdmin):
    list_display = ('materialId', 'categoryId')
    search_fields = list_display
    list_filter = list_display