
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

