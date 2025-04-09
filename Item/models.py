from django.db import models

from Order.models import Order
from Supplier.models import Supplier


class ItemTypeDef(models.IntegerChoices):
    """ 物品类型定义
    """
    PART = 1, '零件'
    ASSEMBLE = 2, '装配'


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
    cost = models.IntegerField(default=0, verbose_name='成本', help_text='成本')  # 单位是分
    sell_price = models.IntegerField(default=0, verbose_name='销售单价', help_text='销售单价')  # 单位是分
    model = models.CharField(max_length=128, blank=True, null=True, verbose_name='型号', help_text='型号')
    num = models.IntegerField(default=1, verbose_name='数量', help_text='数量')
    jet_position = models.CharField(max_length=128, null=True, blank=True, verbose_name='工位号', help_text='工位号')
    item_number = models.CharField(max_length=128, null=True, blank=True, verbose_name='物品编号', help_text='物品编号')
    description = models.TextField(null=True, blank=True, verbose_name='描述', help_text='描述')
    material = models.CharField(max_length=128, null=True, blank=True, verbose_name='材料', help_text='材料')
    weight = models.IntegerField(null=True, blank=True, verbose_name='重量', help_text='重量')
    revision = models.CharField(max_length=128, blank=True, null=True, verbose_name='修订版本', help_text='修订版本')
    uom = models.CharField(max_length=128, blank=True, null=True, verbose_name='计量单位', help_text='计量单位')
    line_type = models.CharField(max_length=128, blank=True, null=True, verbose_name='产线类型', help_text='产线类型')
    supply_type = models.CharField(max_length=128, blank=True, null=True, verbose_name='补充类型', help_text='补充类型')
    eco_number = models.CharField(max_length=128, blank=True, null=True, verbose_name='eco数', help_text='eco数')
    danieli_standard = models.CharField(max_length=128, blank=True, null=True, verbose_name='达涅利标准', help_text='达涅利标准')
    classification = models.CharField(max_length=128, blank=True, null=True, verbose_name='类别', help_text='类别')
    paint_type = models.CharField(max_length=128, blank=True, null=True, verbose_name='油漆种类', help_text='油漆种类')
    color_number = models.CharField(max_length=128, blank=True, null=True, verbose_name='色号', help_text='色号')
    packing_number = models.CharField(max_length=128, blank=True, null=True, verbose_name='箱单号', help_text='箱单号')
    pay_money_list = models.JSONField(default=list, verbose_name='付款', help_text='付款')  # 单位是分
    receive_goods_date_list = models.JSONField(default=list, verbose_name='收货日期列表', help_text='收货日期列表')
    send_goods_date_list = models.JSONField(default=list, verbose_name='发货日期列表', help_text='发货日期列表')
    contract_number = models.CharField(max_length=128, blank=True, null=True, verbose_name='合同号', help_text='合同号')
    supplier = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.PROTECT, verbose_name='供应商', help_text='供应商')
    item_type = models.IntegerField(choices=ItemTypeDef.choices, default=ItemTypeDef.PART, verbose_name='物品类型', help_text='物品类型')

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
