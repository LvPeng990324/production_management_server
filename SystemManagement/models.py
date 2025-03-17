from django.db import models

from UserManagement.models import User


class UserLog(models.Model):
    """ 用户日志
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='关联的用户', help_text='关联的用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间', help_text='记录时间')
    action = models.CharField(max_length=255, verbose_name='动作', help_text='动作')
    detail = models.TextField(verbose_name='详情', help_text='详情')

    class Meta:
        verbose_name_plural = '用户日志'
        verbose_name = '用户日志'

    def __str__(self):
        return '{}-{}-{}'.format(self.user.name, self.action, self.create_time)
