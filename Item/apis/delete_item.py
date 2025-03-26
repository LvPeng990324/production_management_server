from Item.models import Item

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
def delete_item(request):
    """ 删除物品
    POST请求
    """
    item_id = request.json.get('item_id')

    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": '该物品不存在',
        })

    # 缓存日志信息
    item_name = item.name

    item.delete()

    # 记录用户日志
    add_user_log(
        request=request,
        action='删除物品',
        detail=f'{item_name}',
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
