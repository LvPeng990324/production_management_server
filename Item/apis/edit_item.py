from Item.models import Item
from Item.models import InspectionCode
from Order.models import Order

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.data_covert import yuan_to_fen
from utils.data_covert import fen_to_yuan
from utils.permission_check import login_required


@login_required
def edit_item(request):
    """ 编辑物品
    POST请求
    """
    item_id = request.json.get('item_id')
    name = request.json.get('name')
    order_id = request.json.get('order_id')
    parent_item_id = request.json.get('parent_item_id')
    cost = yuan_to_fen(request.json.get('cost'))
    inspection_code_id_list = request.json.get('inspection_code_id_list')

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

    # 记录本次修改的内容描述
    edit_log_str = ''

    # 修改
    if name != item.name:
        edit_log_str += f'名字：{item.name} -> {name}\n'
        item.name = name

    if order != item.order:
        edit_log_str += f'订单：{str(item.order)} -> {str(order)}\n'
        item.order = order

    if parent_item != item.parent_item:
        edit_log_str += f'上级物品：{str(item.parent_item)} -> {parent_item}\n'
        item.parent_item = parent_item

    if cost != item.cost:
        edit_log_str += f'成本：{fen_to_yuan(item.cost)} -> {fen_to_yuan(cost)}\n'
        item.cost = cost

    inspection_codes = InspectionCode.objects.filter(id__in=inspection_code_id_list)
    old_inspection_code_name_set = set(item.inspection_codes.values_list('name', flat=True))
    new_inspection_code_name_set = set(inspection_codes.values_list('name', flat=True))
    if old_inspection_code_name_set != new_inspection_code_name_set:
        edit_log_str += f'检验代码：{str(old_inspection_code_name_set)} -> {str(new_inspection_code_name_set)}\n'
        item.inspection_codes.set(inspection_codes)

    item.save()

    # 记录用户日志
    add_user_log(
        request=request,
        action='编辑物品',
        detail=edit_log_str,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
