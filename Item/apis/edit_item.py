from Item.models import Item
from Order.models import Order

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def edit_item(request):
    """ 编辑物品
    POST请求
    """
    item_id = request.json.get('item_id')
    name = request.json.get('name')
    order_id = request.json.get('order_id')
    parent_item_id = request.json.get('parent_item_id')

    # 转为对象
    order = None
    parent_item = None
    try:
        if order_id:
            order = Order.objects.get(id=order_id)
        if parent_item_id:
            parent_item = Item.objects.get(id=parent_item_id)
    except Order.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": "该订单不存在",
        })
    except Item.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": "该上级物品不存在",
        })

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

    if order != item.order:
        edit_log_record['order'] = [str(item.order), str(order)]
        item.order = order

    if parent_item != item.parent_item:
        edit_log_record['parent_item'] = [str(parent_item), str(parent_item)]
        item.parent_item = parent_item

    item.save()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
