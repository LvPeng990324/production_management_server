from Item.models import Item
from Item.models import InspectionCode
from Order.models import Order

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.data_covert import yuan_to_fen
from utils.data_covert import fen_to_yuan
from utils.data_covert import get_list_default_value
from utils.data_covert import set_list_value_by_index
from utils.permission_check import login_required
from utils.data_calc import check_item_circle_quote


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
    sell_price = yuan_to_fen(request.json.get('sell_price'))
    model = request.json.get('model')
    inspection_code_id_list = request.json.get('inspection_code_id_list')
    num = request.json.get('num')
    jet_position = request.json.get('jet_position')
    item_number = request.json.get('item_number')
    description = request.json.get('description')
    material = request.json.get('material')
    weight = request.json.get('weight')
    revision = request.json.get('revision')
    uom = request.json.get('uom')
    line_type = request.json.get('line_type')
    supply_type = request.json.get('supply_type')
    eco_number = request.json.get('eco_number')
    danieli_standard = request.json.get('danieli_standard')
    classification = request.json.get('classification')
    paint_type = request.json.get('paint_type')
    color_number = request.json.get('colcr_number')
    packing_number = request.json.get('packing_number')
    pay_money_1 = yuan_to_fen(request.json.get('pay_money_1'))
    pay_money_2 = yuan_to_fen(request.json.get('pay_money_2'))
    receive_goods_date_1 = request.json.get('receive_goods_date_1')
    receive_goods_date_2 = request.json.get('receive_goods_date_2')
    send_goods_date_1 = request.json.get('send_goods_date_1')
    send_goods_date_2 = request.json.get('send_goods_date_2')

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
            "message": "该订单不存在",
        })
    except Item.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "该上级物品不存在",
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

    if sell_price != item.sell_price:
        edit_log_str += f'销售单价：{fen_to_yuan(item.sell_price)} -> {fen_to_yuan(sell_price)}\n'
        item.sell_price = sell_price

    if model != item.model:
        edit_log_str += f'型号：{item.cost} -> {model}\n'
        item.model = model

    if num != item.num:
        edit_log_str += f'数量：{item.num} -> {num}\n'
        item.num = num

    if jet_position != item.jet_position:
        edit_log_str += f'JetPosition：{item.jet_position} -> {jet_position}\n'
        item.jet_position = jet_position

    if item_number != item.item_number:
        edit_log_str += f'ItemNumber：{item.item_number} -> {item_number}\n'
        item.item_number = item_number

    if description != item.description:
        edit_log_str += f'Description：{item.description} -> {description}\n'
        item.description = description

    if material != item.material:
        edit_log_str += f'Material：{item.material} -> {material}\n'
        item.material = material

    if weight != item.weight:
        edit_log_str += f'Weight：{item.weight} -> {weight}\n'
        item.weight = weight

    if revision != item.revision:
        edit_log_str += f'Revision：{item.revision} -> {revision}\n'
        item.revision = revision

    if uom != item.uom:
        edit_log_str += f'Uom：{item.uom} -> {uom}\n'
        item.uom = uom

    if line_type != item.line_type:
        edit_log_str += f'LineType：{item.line_type} -> {line_type}\n'
        item.line_type = line_type

    if supply_type != item.supply_type:
        edit_log_str += f'SupplyType：{item.supply_type} -> {supply_type}\n'
        item.supply_type = supply_type

    if eco_number != item.eco_number:
        edit_log_str += f'EcoNumber：{item.eco_number} -> {eco_number}\n'
        item.eco_number = eco_number

    if danieli_standard != item.danieli_standard:
        edit_log_str += f'DanieliStandard：{item.danieli_standard} -> {danieli_standard}\n'
        item.danieli_standard = danieli_standard

    if classification != item.classification:
        edit_log_str += f'Classification：{item.classification} -> {classification}\n'
        item.classification = classification

    if paint_type != item.paint_type:
        edit_log_str += f'油漆种类：{item.paint_type} -> {paint_type}\n'
        item.paint_type = paint_type

    if color_number != item.color_number:
        edit_log_str += f'色号：{item.color_number} -> {color_number}\n'
        item.color_number = color_number

    if packing_number != item.packing_number:
        edit_log_str += f'箱单号：{item.packing_number} -> {packing_number}\n'
        item.packing_number = packing_number

    inspection_codes = InspectionCode.objects.filter(id__in=inspection_code_id_list)
    old_inspection_code_name_set = set(item.inspection_codes.values_list('name', flat=True))
    new_inspection_code_name_set = set(inspection_codes.values_list('name', flat=True))
    if old_inspection_code_name_set != new_inspection_code_name_set:
        edit_log_str += f'检验代码：{str(old_inspection_code_name_set)} -> {str(new_inspection_code_name_set)}\n'
        item.inspection_codes.set(inspection_codes)

    pay_money_list_1 = get_list_default_value(data=item.pay_money_list, index=0, default=0)
    pay_money_list_2 = get_list_default_value(data=item.pay_money_list, index=1, default=0)
    if pay_money_list_1 != pay_money_1:
        edit_log_str += f'付款1：{fen_to_yuan(pay_money_list_1)} -> {fen_to_yuan(pay_money_1)}\n'
        item.pay_money_list = set_list_value_by_index(data=item.pay_money_list, index=0, value=pay_money_1, default=0)
    if pay_money_list_2 != pay_money_2:
        edit_log_str += f'付款2：{fen_to_yuan(pay_money_list_2)} -> {fen_to_yuan(pay_money_2)}\n'
        item.pay_money_list = set_list_value_by_index(data=item.pay_money_list, index=1, value=pay_money_2, default=0)

    receive_goods_date_list_1 = get_list_default_value(data=item.receive_goods_date_list, index=0, default=0)
    receive_goods_date_list_2 = get_list_default_value(data=item.receive_goods_date_list, index=1, default=0)
    if receive_goods_date_list_1 != receive_goods_date_1:
        edit_log_str += f'收货1：{receive_goods_date_list_1} -> {receive_goods_date_1}\n'
        item.receive_goods_date_list = set_list_value_by_index(data=item.receive_goods_date_list, index=0, value=receive_goods_date_1, default='')
    if receive_goods_date_list_2 != receive_goods_date_2:
        edit_log_str += f'收货2：{receive_goods_date_list_2} -> {receive_goods_date_2}\n'
        item.receive_goods_date_list = set_list_value_by_index(data=item.receive_goods_date_list, index=1, value=receive_goods_date_2, default='')

    send_goods_date_list_1 = get_list_default_value(data=item.send_goods_date_list, index=0, default=0)
    send_goods_date_list_2 = get_list_default_value(data=item.send_goods_date_list, index=1, default=0)
    if send_goods_date_list_1 != send_goods_date_1:
        edit_log_str += f'发货1：{send_goods_date_list_1} -> {send_goods_date_1}\n'
        item.send_goods_date_list = set_list_value_by_index(data=item.send_goods_date_list, index=0, value=send_goods_date_1, default='')
    if send_goods_date_list_2 != send_goods_date_2:
        edit_log_str += f'发货2：{send_goods_date_list_2} -> {send_goods_date_2}\n'
        item.send_goods_date_list = set_list_value_by_index(data=item.send_goods_date_list, index=1, value=send_goods_date_2, default='')

    # 检查循环引用
    if not check_item_circle_quote(item=item):
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "操作会导致物品循环引用，检查上级物品合理性",
        })

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
