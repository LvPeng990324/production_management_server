from django.urls import path

from UserManagement.apis.login import login
from UserManagement.apis.get_user_info import get_user_info
from UserManagement.apis.change_self_info import change_self_info


app_name = 'UserManagement'

urlpatterns = [
    # 登录
    path('login/', login, name='login'),
    # 获取用户信息
    path('get-user-info/', get_user_info, name='get_user_info'),
    # 更改自己信息
    path('change-self-info/', change_self_info, name='change_self_info'),
]