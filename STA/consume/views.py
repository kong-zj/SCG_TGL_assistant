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
class ProductConsumeViewSet(viewsets.GenericViewSet):
      
    # 查一个
    def detailed_retrieve(self, request, product_pk):
        # 使用 cursor，完全跨过模型类操作数据库
        cursor = connections['tgl'].cursor()
        params = [product_pk]
        cursor.execute(originalSql.product_consume_get_detailed_sql(), params)
        # 结果是字典列表（可能为空）
        res_dict_list = public_func.dictfetchall(cursor)
        # 构建树形结构 mixTimes:各个具体成分重量
        mixTimes_key_dict = {}
        for dict in res_dict_list:
            # 首次将数据插入 key为 dict['mixTimes'] 的value(列表)中，此时key和value(列表)都不存在，要初始化
            if dict['mixTimes'] not in mixTimes_key_dict:
                mixTimes_key_dict[dict['mixTimes']] = []
            value = {'bigMaterialName':dict['bigMaterialName'], 'smallMaterialName':dict['smallMaterialName'], 'defaultKilogram':dict['defaultKilogram'], 'realKilogram':dict['realKilogram'], 'aggregateHasWaterPercent':dict['aggregateHasWaterPercent'], 'realKilogramWithoutWater':dict['realKilogramWithoutWater']}
            mixTimes_key_dict[dict['mixTimes']].append(value)
            # 格式: dict{mixTimes: list[各个成分的字典] } }
        json_res = {
            'count': len(mixTimes_key_dict)-1, # 分为几盘搅拌
            'results': mixTimes_key_dict
        }
        return JsonResponse(json_res)
    
    
    def brief_retrieve(self, request, product_pk):
        # 使用 cursor，完全跨过模型类操作数据库
        cursor = connections['tgl'].cursor()
        params = [product_pk]
        cursor.execute(originalSql.product_consume_get_brief_sql(), params)
        # 结果是字典列表（可能为空）
        res_dict_list = public_func.dictfetchall(cursor)
        # 格式: list[各个成分的字典]
        json_res = {
            'results': res_dict_list
        }
        return JsonResponse(json_res)
