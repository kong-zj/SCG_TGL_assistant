import re
  
# 将查询出的多行数据序列化为字典列表 dict_list
def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


# 将查询出的单行数据序列化为字典 dict
def dictfetchone(cursor):
    """注意
    list(cursor) 与 cursor.fetchone() 冲突,
    使用了 cursor.fetchone() 就不要使用 list(cursor)
    """
    # 结果若是空，返回空
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()
    # init
    res = None
    if row is not None:
        res = dict(zip(columns, row))        
    return res

# 解析 order_adjustable_recipe表中的 recipeContent列
# 字符串，内容格式为 "{bigMaterialName(smallMaterialName)=usageKilogram}{...}"
def recipeContent_to_dict_list(recipeContent):
    # init
    recipeContent_dict_list = []
    each_recipe_str_list = re.split(pattern=r'[{}]', string=recipeContent)
    # filter()函数的返回值是迭代器，要转换为list
    each_recipe_str_list = list(filter(lambda eachRecipeString: eachRecipeString != '', each_recipe_str_list))
    for each_recipe_str in each_recipe_str_list:
        # 字符串，内容格式为"{bigMaterialName(smallMaterialName)=usageKilogram}
        bigAndsmallMaterialName, usageKilogram = re.split(pattern=r'[=]', string=each_recipe_str, maxsplit=1)
        bigMaterialName, smallMaterialName, discard_str = re.split(pattern=r'[()]', string=bigAndsmallMaterialName, maxsplit=2)
        value = {'bigMaterialName':bigMaterialName, 'smallMaterialName':smallMaterialName, 'usageKilogram':usageKilogram}
        recipeContent_dict_list.append(value)
    return recipeContent_dict_list

