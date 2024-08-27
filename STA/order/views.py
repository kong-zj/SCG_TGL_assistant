import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from django.db import connections
from .original_sql import originalSql
from . import public_func



# ReadOnly
class OrderViewSet(viewsets.GenericViewSet):
    
    # 查全部，内容过多，考虑分页
    def list(self, request):
        cursor = connections['tgl'].cursor()
        cursor.execute(originalSql.order_all_sql())
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
        cursor.execute(originalSql.order_get_sql(pk))
        # 结果是字典（可能为空）
        res_dict = public_func.dictfetchone(cursor)
        # init
        json_res = {
            "detail": "No Order matches the given query."
        }
        status_res = status.HTTP_404_NOT_FOUND
        if res_dict is not None:
             json_res = res_dict
             status_res = status.HTTP_200_OK
        return JsonResponse(data=json_res,status=status_res)
    
    