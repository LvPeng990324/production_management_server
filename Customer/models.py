from django.db import models


class Customer(models.Model):
    """ 客户
    """
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name='名称', help_text='名称')
    contact_person = models.CharField(max_length=128, blank=True, null=True, verbose_name='联系人', help_text='联系人')
    phone = models.CharField(max_length=128, blank=True, null=True, verbose_name='电话', help_text='电话')
    email = models.CharField(max_length=128, blank=True, null=True, verbose_name='邮箱', help_text='邮箱')
    tax_number = models.CharField(max_length=128, blank=True, null=True, verbose_name='税号', help_text='税号')
    address = models.CharField(max_length=128, blank=True, null=True, verbose_name='地址', help_text='地址')
    bank_card_number = models.CharField(max_length=128, blank=True, null=True, verbose_name='银行卡号', help_text='银行卡号')
    bank_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='开户行', help_text='开户行')

    class Meta:
        verbose_name_plural = '客户'
        verbose_name = '客户'

    def __str__(self):
        return f'{self.id} {self.name}'
