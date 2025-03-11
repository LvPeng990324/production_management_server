from django.db import models

from Order.models import Order


class InspectionCode(models.Model):
    """ 检验代码
    """
    name = models.CharField(max_length=128, verbose_name='名称', help_text='名称')

    class Meta:
        verbose_name_plural = '检验代码'
        verbose_name = '检验代码'

    def __str__(self):
        return f'{self.id} {self.name}'

class Item(models.Model):
    """ 物品
    """
    name = models.CharField(max_length=32, verbose_name='名称', help_text='名称')
    order = models.ForeignKey(to=Order, null=True, blank=True, on_delete=models.PROTECT, verbose_name='订单', help_text='订单')
    parent_item = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT, verbose_name='上级物品', help_text='上级物品')
    inspection_codes = models.ManyToManyField(to=InspectionCode, verbose_name='检验代码', help_text='检验代码')

    class Meta:
        verbose_name_plural = '物品'
        verbose_name = '物品'

    def __str__(self):
        return f'{self.id} {self.name}'


class TechnicalChange(models.Model):
    """ 技术变更
    """
    name = models.CharField(max_length=32, verbose_name='名称', help_text='名称')
    item = models.ForeignKey(to=Item, null=True, blank=True, on_delete=models.PROTECT, verbose_name='物品', help_text='物品')
    
    class Meta:
        verbose_name_plural = '技术变更'
        verbose_name = '技术变更'

    def __str__(self):
        return f'{self.id} {self.name}'
