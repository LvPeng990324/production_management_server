from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response


def get_user_info(request):
    """ 获取用户信息
    GET请求
    """
    return json_response(code=ERROR_CODE.SUCCESS, data={
        "username": "admin11",
    })
