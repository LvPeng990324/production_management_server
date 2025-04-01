from Item.models import TechnicalChange
from Item.models import Item

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
def edit_technical_change(request):
    """ 编辑技术变更
    POST请求
    """
    technical_change_id = request.json.get('technical_change_id')
    name = request.json.get('name')
    item_id = request.json.get('item_id')

    try:
        technical_change = TechnicalChange.objects.get(id=technical_change_id)
    except TechnicalChange.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": '该技术变更不存在',
        })

    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": '该物品不存在',
        })

    # 记录本次修改的内容描述
    edit_log_str = ''

    # 修改
    if name != technical_change.name:
        edit_log_str += f'名字：{technical_change.name} -> {name}\n'
        technical_change.name = name
    
    if item != technical_change.item:
        edit_log_str += f'关联物品：{str(technical_change.item)} -> {str(item)}\n'
        technical_change.item = item

    technical_change.save()

    # 记录用户日志
    add_user_log(
        request=request,
        action='编辑技术变更',
        detail=edit_log_str,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
