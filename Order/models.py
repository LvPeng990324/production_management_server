from django.db import models

from UserManagement.models import User
from Customer.models import Customer


class OrderStatus(models.IntegerChoices):
    """ 订单状态
    """
    PENDING = 1, '待启动'
    DOING = 2, '制作中'
    FINISH = 3, '已完成'


class Order(models.Model):
    """ 订单
    """
    order_num = models.CharField(max_length=32, verbose_name='订单号', help_text='订单号')
    order_status = models.IntegerField(choices=OrderStatus.choices, verbose_name='订单状态', help_text='订单状态')
    delivery_date = models.DateField(blank=True, null=True, verbose_name='交货日期', help_text='交货日期')
    collect_money_list = models.JSONField(default=list, verbose_name='收款列表', help_text='收款列表')
    worker = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='负责人', help_text='负责人')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='客户', help_text='客户')
    pay_method = models.CharField(max_length=128, blank=True, null=True, verbose_name='付款方式', help_text='付款方式')

    class Meta:
        verbose_name_plural = '订单'
        verbose_name = '订单'

    def __str__(self):
        return f'{self.id} {self.order_num}'
