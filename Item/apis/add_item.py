from Item.models import Item
from Item.models import InspectionCode
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
    inspection_code_id_list = request.json.get('inspection_code_id_list')

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

    # 添加检验代码
    if inspection_code_id_list:
        inspection_codes = InspectionCode.objects.filter(id__in=inspection_code_id_list)
        new_item.inspection_codes.set(inspection_codes)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
