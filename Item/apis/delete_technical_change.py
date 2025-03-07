from Item.models import TechnicalChange

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def delete_technical_change(request):
    """ 删除技术变更
    POST请求
    """
    technical_change_id = request.json.get('technical_change_id')

    try:
        technical_change = TechnicalChange.objects.get(id=technical_change_id)
    except TechnicalChange.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": '该技术变更不存在',
        })

    technical_change.delete()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
