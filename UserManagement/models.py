from django.db import models


class User(models.Model):
    """ 用户
    """
    name = models.CharField(max_length=32, verbose_name='姓名', help_text='姓名')
    phone = models.CharField(max_length=16, verbose_name='手机号', help_text='手机号')
    password_md5 = models.CharField(max_length=128, verbose_name='密码md5', help_text='密码md5')
    
    class Meta:
        verbose_name_plural = '用户'
        verbose_name = '用户'

    def __str__(self):
        return f'{self.id} {self.name}'

