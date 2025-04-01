# 权限检查器们
from django.contrib import messages
from django.shortcuts import redirect

from UserManagement.models import User

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def login_required(func):
    """ 检查是否登录装饰器
    """
    def wrapper(request, *args, **kwargs):
        # 读取session中记录
        user_id = request.session.get('user_id')
        if not user_id or not User.objects.filter(id=user_id).exists():
            # 没有登录信息，拦截
            request.session.flush()  # 清空session信息
            return json_response(code=ERROR_CODE.TOKEN_EXPIRE, data={
                'message': "登录信息已过期，重新登录",
            })
        # 已登录，放行
        return func(request, *args, **kwargs)
    return wrapper