from Item.models import InspectionCode

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def edit_inspection_code(request):
    """ 编辑检验代码
    POST请求
    """
    inspection_code_id = request.json.get('inspection_code_id')
    name = request.json.get('name')

    try:
        inspection_code = InspectionCode.objects.get(id=inspection_code_id)
    except InspectionCode.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": '该检验代码不存在',
        })

    # 记录本次修改的内容
    # {字段名: [旧值, 新值]}
    edit_log_record = {}

    # 修改
    if name != inspection_code.name:
        edit_log_record['name'] = [inspection_code.name, name]
        inspection_code.name = name

    inspection_code.save()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
