from django.urls import path

from UserManagement.apis.login import login
from UserManagement.apis.get_user_info import get_user_info


app_name = 'UserManagement'

urlpatterns = [
    # 登录
    path('login/', login, name='login'),
    # 获取用户信息
    path('get-user-info/', get_user_info, name='get_user_info'),
]