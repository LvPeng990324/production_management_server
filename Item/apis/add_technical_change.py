from Item.models import TechnicalChange

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def add_technical_change(request):
    """ 新增技术变更
    POST请求
    """
    name = request.json.get('name')

    TechnicalChange.objects.create(
        name=name,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
