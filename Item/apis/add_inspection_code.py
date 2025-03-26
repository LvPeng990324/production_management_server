from Item.models import InspectionCode

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
def add_inspection_code(request):
    """ 新增检验代码
    POST请求
    """
    name = request.json.get('name')

    InspectionCode.objects.create(
        name=name,
    )

    # 记录用户日志
    add_user_log(
        request=request,
        action='新增检验代码',
        detail=f'{name}',
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
