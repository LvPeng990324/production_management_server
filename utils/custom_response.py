from django.http import JsonResponse
from enum import Enum


# 业务错误码定义
class ERROR_CODE(Enum):
    SUCCESS = 0
    NOT_FOUND = 1
    AUTH_FAIL = 2
    ILLEGAL = 3

    TOKEN_EXPIRE = 401


def json_response(code: ERROR_CODE, data: dict):
    return JsonResponse(data={
        "code": code.value,
        "data": data,
    })
