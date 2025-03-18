from Item.models import InspectionCode

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log


def delete_inspection_code(request):
    """ 删除检验代码
    POST请求
    """
    inspection_code_id = request.json.get('inspection_code_id')

    try:
        inspection_code = InspectionCode.objects.get(id=inspection_code_id)
    except InspectionCode.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": '该检验代码不存在',
        })
    
    # 缓存日志用字段
    inspection_code_name = inspection_code.name

    inspection_code.delete()

    # 记录用户日志
    add_user_log(
        request=request,
        action='删除检验代码',
        detail=f'{inspection_code_name}',
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
