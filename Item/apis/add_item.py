from Item.models import Item
from Order.models import Order

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def add_item(request):
    """ 新增物品
    POST请求
    """
    name = request.json.get('name')
    order_id = request.json.get('order_id')
    parent_item_id = request.json.get('parent_item_id')

    # 实例化基础属性
    new_item = Item(
        name=name,
    )

    # 判断添加关联订单
    if order_id:
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return json_response(code=ERROR_CODE.NOT_FOUND, data={
                "msg": '该订单不存在',
            })
        new_item.order = order

    # 判断添加上级物品
    if parent_item_id:
        try:
            parent_item = Item.objects.get(id=parent_item_id)
        except Item.DoesNotExist:
            return json_response(code=ERROR_CODE.NOT_FOUND, data={
                "msg": "该上级物品不存在",
            })
        new_item.parent_item = parent_item
    
    # 提交
    new_item.save()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
