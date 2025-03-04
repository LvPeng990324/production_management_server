from Item.models import Item

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def edit_item(request):
    """ 编辑物品
    POST请求
    """
    item_id = request.json.get('item_id')
    name = request.json.get('name')

    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
        "msg": '该物品不存在',
    })

    # 记录本次修改的内容
    # {字段名: [旧值, 新值]}
    edit_log_record = {}

    # 修改
    if name != item.name:
        edit_log_record['name'] = [item.name, name]
        item.name = name

    item.save()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
