from django.db import models

class Supplier(models.Model):
    """ 供应商
    """
    name = models.CharField(max_length=32, verbose_name='名字', help_text='名字')
    phone = models.CharField(max_length=16, verbose_name='手机号', help_text='手机号')

    class Meta:
        verbose_name_plural = '供应商'
        verbose_name = '供应商'

    def __str__(self):
        return f'{self.id} {self.name}'
