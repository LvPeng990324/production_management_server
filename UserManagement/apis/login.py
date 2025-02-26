from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response


def login(request):
    """ 登录
    POST请求
    """
    return json_response(code=ERROR_CODE.SUCCESS, data={
        "token": "token-admin",
    })
