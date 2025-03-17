from django.urls import path

from SystemManagement.apis.get_user_log_list import get_user_log_list


app_name = 'SystemManagement'

urlpatterns = [
    # 获取用户日志列表
    path('get-user-log-list/', get_user_log_list, name='get_user_log_list'),
]