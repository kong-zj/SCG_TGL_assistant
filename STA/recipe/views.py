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
    
    def list_original_inner(self, pk):
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
        # 格式: dict{defaultDateTime: dict{machineId: list[各个成分的字典] } }
        defaultDateTime_key_dict = {}
        # 如果machineId_key_dict字典非空，那么指定defaultDateTime为0
        if machineId_key_dict:
            defaultDateTime_key_dict = {'0': machineId_key_dict}
        return defaultDateTime_key_dict
    
    def list_adjustable_inner(self, pk):
        cursor = connections['tgl'].cursor()
        # 原始配比
        cursor.execute(originalSql.order_adjustable_recipe_all_sql(), (pk, ))
        # 结果是字典列表（可能为空）
        res_dict_list = public_func.dictfetchall(cursor)
        # 构建树形结构 adjustDateTime:各个machineId的调整
        adjustDateTime_key_dict = {}
        for dict in res_dict_list:
            # 首次将数据插入 key为 dict['adjustDateTime'] 的value(字典)中，此时key和value(列表)都不存在，要初始化
            if dict['adjustDateTime'] not in adjustDateTime_key_dict:
                adjustDateTime_key_dict[dict['adjustDateTime']] = {}
                # 解析 dict['recipeContent']
                # 每种成分解析为一个字典，返回字典列表
                recipeContent_dict_list = public_func.recipeContent_to_dict_list(dict['recipeContent'])
                format_machineId = dict['machineId']
                # 施工 -> 0
                if '施工' == format_machineId:
                    format_machineId = 0
            # value = {'machineId':format_machineId, 'recipeContent':recipeContent_dict_list}
            value = {format_machineId:recipeContent_dict_list}
            # 格式: dict{adjustDateTime: dict{machineId: list[各个成分的字典] } }
            adjustDateTime_key_dict[dict['adjustDateTime']] = value
        return adjustDateTime_key_dict
    
    # 查全部
    def list(self, request, pk):
        defaultDateTime_key_dict = self.list_original_inner(pk)
        adjustDateTime_key_dict = self.list_adjustable_inner(pk)
        # 字典二合一
        dateTime_key_dict = {**defaultDateTime_key_dict, **adjustDateTime_key_dict}
        json_res = {
            'count': len(dateTime_key_dict),
            'results': dateTime_key_dict
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
