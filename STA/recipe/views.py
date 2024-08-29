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
class SystemRecipeViewSet(viewsets.GenericViewSet):
    
    # 查全部，内容过多，考虑分页
    def brief_list(self, request):
        # 获取get参数
        status_input = request.GET.get('status')
        cursor = connections['tgl'].cursor()
        # init params
        # f"%%" 相当于 LIKE 运算中的 全匹配
        status_format = f"%%"
        if status_input:
            #匹配当中若干字符
            if '1' == status_input:
                status_input = '正在使用'
            elif '2' == status_input:
                status_input = '停止使用'
            elif '3' == status_input:
                status_input = '尚未使用'  
            else:
                json_res = {
                    'detail': 'status must be one of 1,2,3.',
                }
                status_res = status.HTTP_400_BAD_REQUEST
                return JsonResponse(data=json_res,status=status_res)
            status_format = f"%{status_input}%"
        params = [status_format]
        cursor.execute(originalSql.system_brief_recipe_all_sql(), params)
        # 结果是字典列表（可能为空）
        res_dict_list = public_func.dictfetchall(cursor)
        json_res = {
            'count': len(res_dict_list),
            'results': res_dict_list
        }
        return JsonResponse(json_res)
    
    
    # 查一个，返回详细信息（包括具体配比）
    def detailed_retrieve(self, request, pk):
        cursor = connections['tgl'].cursor()
        cursor.execute(originalSql.system_brief_recipe_get_sql(), (pk, ))
        # 结果是字典（可能为空）
        res_dict = public_func.dictfetchone(cursor)
        # init
        json_res = {
            'detail': 'No SystemRecipe matches the given query.'
        }
        status_res = status.HTTP_404_NOT_FOUND
        if res_dict is not None:
            json_res = res_dict
            status_res = status.HTTP_200_OK
            # 查具体配比
            cursor.execute(originalSql.system_detailed_recipe_get_sql(), (pk, ))
            # 结果是字典列表（可能为空）
            res_dict_list = public_func.dictfetchall(cursor)
            json_res['detailed_recipe'] = res_dict_list
        return JsonResponse(data=json_res,status=status_res)



# ReadOnly
class OrderRecipeViewSet(viewsets.GenericViewSet):
    
    # 查全部
    def list(self, request, pk):
        cursor = connections['tgl'].cursor()
        # 原始配比
        cursor.execute(originalSql.order_original_recipe_all_sql(), (pk, ))
        # 结果是字典列表（可能为空）
        res_dict_list = public_func.dictfetchall(cursor)
        # 构建树形结构 machineId:各个具体成分重量
        machineId_key_dict = {}
        for dict in res_dict_list:
            # 首次将数据插入 key为 dict['machineId'] 的value(列表)中，此时key和value(列表)都不存在，要初始化
            if dict['machineId'] not in machineId_key_dict:
                machineId_key_dict[dict['machineId']] = []
            value = {'bigMaterialName':dict['bigMaterialName'], 'smallMaterialName':dict['smallMaterialName'], 'usageKilogram':dict['usageKilogram']}
            machineId_key_dict[dict['machineId']].append(value)
        print(machineId_key_dict)
        json_res = {
            'count': len(machineId_key_dict),
            'results': machineId_key_dict
        }
        return JsonResponse(json_res)
    
    
    
# ReadOnly
class ProductRecipeViewSet(viewsets.GenericViewSet):
    
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
