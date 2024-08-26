from django.db import models


class Category(models.Model):
    categoryId = models.AutoField(primary_key=True, help_text='分类Id', verbose_name='分类Id')
    categoryName = models.CharField(max_length=24, help_text='分类名称', verbose_name='分类名称')
    
    class Meta:
        verbose_name = '原料分类信息'
        verbose_name_plural = verbose_name
        ordering = ['categoryId']

    def __str__(self):
        return self.categoryId + ':' + self.categoryName