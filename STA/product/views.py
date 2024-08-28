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
class ProductViewSet(viewsets.GenericViewSet):
    
    # 查全部，内容过多，考虑分页
    def list(self, request):
        # 获取get参数
        productDate_input = request.GET.get('productDate')
        coprojlpName_input = request.GET.get('coprojlpName')
        orderId_input = request.GET.get('orderId')
        cursor = connections['tgl'].cursor()
        # init params
        # f"%%" 相当于 LIKE 运算中的 全匹配
        productDate_format = f"%%"
        coprojlpName_format = f"%%"
        orderId_format = None
        if productDate_input:
            #匹配开头若干字符
            productDate_format = f"{productDate_input}%"
        if coprojlpName_input:
            # f"%{coprojlpName_input}%" 相当于 LIKE 运算中的 任意位置匹配
            coprojlpName_format = f"%{coprojlpName_input}%"
        if orderId_input:
            try:
                # str转型为int，防止sql注入
                orderId_format = int(orderId_input)
            # 如果无法int转型
            except ValueError as ErrMessage:
                json_res = {
                    'detail': 'orderId must be int.',
                    'errmessage': str(ErrMessage)
                }
                status_res = status.HTTP_400_BAD_REQUEST
                return JsonResponse(data=json_res,status=status_res)
            # 其他异常
            except Exception as ErrMessage:
                json_res = {
                    'detail': 'Serious error.',
                    'errmessage': str(ErrMessage)
                }
                status_res = status.HTTP_400_BAD_REQUEST
                return JsonResponse(data=json_res,status=status_res)
        params = [productDate_format, coprojlpName_format, coprojlpName_format, coprojlpName_format]
        # 下策，orderId_format 直接去sql拼接，orderId_format 为 int值 或 None
        cursor.execute(originalSql.product_all_sql(orderId_format), params)
        # 在这里用 cursor.rowcount 判断结果行数是无效的
        # 结果是字典列表（可能为空）
        res_dict_list = public_func.dictfetchall(cursor)
        json_res = {
            'count': len(res_dict_list),
            'results': res_dict_list
        }
        return JsonResponse(json_res)
    
    
    # 查一个，返回详细信息
    def retrieve(self, request, pk):
        cursor = connections['tgl'].cursor()
        cursor.execute(originalSql.product_get_sql(), (pk, ))
        # 结果是字典（可能为空）
        res_dict = public_func.dictfetchone(cursor)
        # init
        json_res = {
            'detail': 'No Product matches the given query.'
        }
        status_res = status.HTTP_404_NOT_FOUND
        if res_dict is not None:
             json_res = res_dict
             status_res = status.HTTP_200_OK
        return JsonResponse(data=json_res,status=status_res)
    
    