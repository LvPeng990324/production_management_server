from Item.models import InspectionCode

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
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
            "message": '该检验代码不存在',
        })

    # 记录本次修改的内容描述
    edit_log_str = ''

    # 修改
    if name != inspection_code.name:
        edit_log_str += f'名字：{inspection_code.name} -> {name}\n'
        inspection_code.name = name

    inspection_code.save()

    # 记录用户日志
    add_user_log(
        request=request,
        action='编辑检验代码',
        detail=edit_log_str,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
