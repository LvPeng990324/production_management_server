from Item.models import Item
from Item.models import InspectionCode
from Order.models import Order

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.data_covert import yuan_to_fen
from utils.permission_check import login_required
from utils.data_calc import check_item_circle_quote


@login_required
def add_item(request):
    """ 新增物品
    POST请求
    """
    name = request.json.get('name')
    order_id = request.json.get('order_id')
    parent_item_id = request.json.get('parent_item_id')
    cost = yuan_to_fen(request.json.get('cost'))
    inspection_code_id_list = request.json.get('inspection_code_id_list')
    num = request.json.get('num')

    # 实例化基础属性
    new_item = Item(
        name=name,
        cost=cost,
        num=num,
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
    
    # 检查是否有循环引用
    if not check_item_circle_quote(item=new_item):
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": "操作会导致物品循环引用，检查上级物品合理性",
        })

    # 提交
    new_item.save()

    # 添加检验代码
    if inspection_code_id_list:
        inspection_codes = InspectionCode.objects.filter(id__in=inspection_code_id_list)
        new_item.inspection_codes.set(inspection_codes)
    
    # 记录用户日志
    order_num = '无'
    if new_item.order:
        order_num = new_item.order.order_num
    parent_item_name = '无'
    if new_item.parent_item:
        parent_item_name = new_item.parent_item.name
    inspection_code_name_list = list(new_item.inspection_codes.values_list('name', flat=True))
    inspection_code_names = '、'.join(inspection_code_name_list)
    add_user_log(
        request=request,
        action=f'新增物品',
        detail=f'''名字：{name}
        关联订单号：{order_num}
        关联上级物品：{parent_item_name}
        成本：{cost / 100}
        数量：num
        检验代码：{inspection_code_names}''',
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
