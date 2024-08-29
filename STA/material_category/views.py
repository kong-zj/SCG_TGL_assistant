import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from .models import Category, MaterialLinkCategory
from .serializers import CategorySerializer, MaterialLinkCategorySerializer
from django.db import connections
from .original_sql import originalSql
from . import public_func


# CURD
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# CURD
class MaterialLinkCategoryViewSet(viewsets.ModelViewSet):
    queryset = MaterialLinkCategory.objects.all()
    serializer_class = MaterialLinkCategorySerializer




# # DRF CBV
# class CourseListDRF(APIView):
#     def get(self, request):
        
#         # queryset = Course.objects.all()
#         # s = CourseSerializer(instance=queryset, many=True)
#         # return Response(data=s.data, status=status.HTTP_200_OK)
    
#     # def post(self, request):
#     #     s = CourseSerializer(data=request.data, partial=True)
#     #     if s.is_valid():
#     #         s.save(teacher=self.request.user)
#     #         return Response(data=s.data, status=status.HTTP_201_CREATED)
#     #     else:
#     #         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)




# ReadOnly
class OriginalMaterialViewSet(viewsets.GenericViewSet):
    
    # 查全部
    def list(self, request):
        # 使用 cursor，完全跨过模型类操作数据库
        cursor = connections['tgl'].cursor()
        cursor.execute(originalSql.original_material_all_sql())
        # 在这里用 cursor.rowcount 判断结果行数是无效的
        # 结果是字典列表（可能为空）
        res_dict_list = public_func.dictfetchall(cursor)
        json_res = {
            'count': len(res_dict_list),
            'results': res_dict_list
        }
        return JsonResponse(json_res)
    
    
    # 查一个
    def retrieve(self, request, pk):
        cursor = connections['tgl'].cursor()
        # 在sql语句中使用%s占位符形式，通过python本身的占位符语法先动态生成完整sql
        cursor.execute(originalSql.original_material_get_sql(), (pk, ))
        # 结果是字典（可能为空）
        res_dict = public_func.dictfetchone(cursor)
        # init
        json_res = {
            'detail': 'No OriginalMaterial matches the given query.'
        }
        status_res = status.HTTP_404_NOT_FOUND
        if res_dict is not None:
            json_res = res_dict
            status_res = status.HTTP_200_OK
        return JsonResponse(data=json_res,status=status_res)
    
    
    

# # 爬取ntgl的数据库，保存到自己的数据库
# @api_view(["POST"])
# def prod_cont(request):
#     if request.method == "POST":
        

#         sql = '''

# '''

#         try:
#             # 拿到ntgldata数据库中，tjlb（生产记录表）和 trwdphb（配合比记录表）的数据
#             with connection['ntgl'].cursor() as cursor:
#                 cursor.execute(sql)
#                 # 字典列表
#                 res_dict_list = dictfetchall(cursor)
#         except Exception as e:
#             return Response(data={"msg": str(e)}, status=status.HTTP_404_NOT_FOUND)
#         # 无异常
#         else:
#             # 压缩数据，格式化数据（去掉前后的空格，和后面的换行符）
#             zip_dict_list = zip_prod_by_order_and_cont(res_dict_list)
#             # 保存到数据库
#             save_prod_cont_data(zip_dict_list)

#             return Response(data=zip_dict_list, status=status.HTTP_200_OK)
#     # 非 GET方法
#     else:
#         return Response(data={"msg": "bad request, 错误的请求方法"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    