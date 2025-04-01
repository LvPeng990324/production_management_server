from UserManagement.models import User

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.data_covert import str_to_md5


def login(request):
    """ 登录
    POST请求
    """
    phone = request.json.get('phone')
    password_md5 = str_to_md5(request.json.get('password') or '')

    try:
        user = User.objects.get(phone=phone)
    except User.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "未找到该用户",
        })

    # 校验密码
    if user.password_md5 != password_md5:
        return json_response(code=ERROR_CODE.AUTH_FAIL, data={
            "message": "密码错误",
        })

    # 记录session信息
    request.session['name'] = user.name
    request.session['phone'] = user.phone
    request.session['user_id'] = user.id

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "token": "token-admin",
    })
