from rest_framework import serializers
from .models import Category, MaterialLinkCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        # 关联数据表（前面不是变量名）
        model = Category
        # 确定需要序列化的字段（返回给用户的具体表中的字段）（前面不是变量名）
        # fields = ['categoryId', 'categoryName']
        # 表示全部字段
        fields = '__all__'
        

class MaterialLinkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialLinkCategory
        fields = '__all__'

