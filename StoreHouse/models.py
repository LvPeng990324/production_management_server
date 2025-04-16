from django.db import models

from Item.models import Item


class StoreHouse(models.Model):
    """ 库存
    """
    item = models.ForeignKey(to=Item, on_delete=models.PROTECT, verbose_name='物品', help_text='物品')
    remain_count = models.IntegerField(verbose_name='余量', help_text='余量')
    operate_log_list = models.JSONField(default=list, verbose_name='操作记录列表', help_text='操作记录列表')

    class Meta:
        verbose_name_plural = '库存'
        verbose_name = '库存'

    def __str__(self):
        return f'{self.id} {self.item.name} {self.remain_count}'
