from django.db import models

class Item(models.Model):
    """ 物品
    """
    name = models.CharField(max_length=32, verbose_name='名称', help_text='名称')

    class Meta:
        verbose_name_plural = '物品'
        verbose_name = '物品'

    def __str__(self):
        return f'{self.id} {self.name}'


class TechnicalChange(models.Model):
    """ 技术变更
    """
    name = models.CharField(max_length=32, verbose_name='名称', help_text='名称')
    
    class Meta:
        verbose_name_plural = '技术变更'
        verbose_name = '技术变更'

    def __str__(self):
        return f'{self.id} {self.name}'


class InspectionCode(models.Model):
    """ 检验代码
    """
    name = models.CharField(max_length=128, verbose_name='名称', help_text='名称')

    class Meta:
        verbose_name_plural = '检验代码'
        verbose_name = '检验代码'

    def __str__(self):
        return f'{self.id} {self.name}'
