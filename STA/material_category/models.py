from django.db import models


# 分类名表
class Category(models.Model):
    categoryId = models.AutoField(primary_key=True, help_text='分类Id', verbose_name='分类Id')
    categoryName = models.CharField(unique=True, max_length=24, help_text='分类名称', verbose_name='分类名称')
    intoStatisticsFlag = models.BooleanField(help_text='是否纳入统计', verbose_name='是否纳入统计')
    
    class Meta:
        verbose_name = '原料分类名信息'
        verbose_name_plural = verbose_name
        ordering = ['categoryId']

    def __str__(self):
        return str(self.categoryId) + ':' + str(self.categoryName)
    
# 连接分类名表（本项目中）和原料名表（TGL中）
class MaterialLinkCategory(models.Model):
    materialId = models.IntegerField(primary_key=True, help_text='原料Id', verbose_name='原料Id') # 不可重复，另一个数据库表的外键
    categoryId = models.ForeignKey(to=Category, on_delete=models.CASCADE, help_text='分类Id', verbose_name='分类Id') # 可重复
    
    class Meta:
        verbose_name = '原料绑定分类信息'
        verbose_name_plural = verbose_name
        ordering = ['categoryId', 'materialId']
