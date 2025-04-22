from django.db import models

from Item.models import Item


class PurchaseRequirement(models.Model):
    """ 采购需求
    """
    item = models.ForeignKey(to=Item, on_delete=models.PROTECT, verbose_name='物品', help_text='物品')
    count = models.IntegerField(verbose_name='数量', help_text='数量')
    date = models.DateField(verbose_name='需求日期', help_text='需求日期')

    class Meta:
        verbose_name_plural = '采购需求'
        verbose_name = '采购需求'

    def __str__(self):
        return f'{self.id} {self.item.name} {self.count} {self.date}'
