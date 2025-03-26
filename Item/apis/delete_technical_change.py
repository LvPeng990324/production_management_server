from Item.models import TechnicalChange

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
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

    # 缓存日志内容
    technical_change_name = technical_change.name

    technical_change.delete()

    # 记录用户日志
    add_user_log(
        request=request,
        action='删除技术变更',
        detail=f'{technical_change_name}',
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
