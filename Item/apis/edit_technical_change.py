from Item.models import TechnicalChange

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def edit_technical_change(request):
    """ 编辑技术变更
    POST请求
    """
    technical_change_id = request.json.get('technical_change_id')
    name = request.json.get('name')

    try:
        technical_change = TechnicalChange.objects.get(id=technical_change_id)
    except TechnicalChange.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
        "msg": '该技术变更不存在',
    })

    # 记录本次修改的内容
    # {字段名: [旧值, 新值]}
    edit_log_record = {}

    # 修改
    if name != technical_change.name:
        edit_log_record['name'] = [technical_change.name, name]
        technical_change.name = name

    technical_change.save()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
