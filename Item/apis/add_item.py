from Item.models import Item
from Item.models import ItemTypeDef
from Item.models import InspectionCode
from Order.models import Order
from Supplier.models import Supplier

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.data_covert import yuan_to_fen
from utils.data_covert import fen_to_yuan
from utils.permission_check import login_required
from utils.data_calc import check_item_circle_quote


@login_required
def add_item(request):
    """ 新增物品
    POST请求
    """
    name = request.json.get('name')
    item_type_value = request.json.get('item_type_value')
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
    contract_number = request.json.get('contract_number')
    supplier_id = request.json.get('supplier_id')

    # 实例化基础属性
    new_item = Item(
        name=name,
        cost=cost,
        sell_price=sell_price,
        model=model,
        num=num,
        jet_position=jet_position,
        item_number=item_number,
        description=description,
        material=material,
        weight=weight,
        revision=revision,
        uom=uom,
        line_type=line_type,
        supply_type=supply_type,
        eco_number=eco_number,
        danieli_standard=danieli_standard,
        classification=classification,
        paint_type=paint_type,
        color_number=color_number,
        packing_number=packing_number,
        pay_money_list=[pay_money_1, pay_money_2],
        receive_goods_date_list=[receive_goods_date_1, receive_goods_date_2],
        send_goods_date_list=[send_goods_date_1, send_goods_date_2],
        contract_number=contract_number,
    )

    # 判断添加关联订单
    if order_id:
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return json_response(code=ERROR_CODE.NOT_FOUND, data={
                "message": '该订单不存在',
            })
        new_item.order = order

    # 判断添加上级物品
    if parent_item_id:
        try:
            parent_item = Item.objects.get(id=parent_item_id)
        except Item.DoesNotExist:
            return json_response(code=ERROR_CODE.NOT_FOUND, data={
                "message": "该上级物品不存在",
            })
        new_item.parent_item = parent_item

    # 判断添加供应商
    if supplier_id:
        try:
            supplier = Supplier.objects.get(id=supplier_id)
        except Supplier.DoesNotExist:
            return json_response(code=ERROR_CODE.NOT_FOUND, data={
                "message": "该供应商不存在",
            })
        new_item.supplier = supplier
    
    # 判断物品类型
    try:
        item_type = ItemTypeDef(item_type_value)
    except ValueError:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "物品类型不存在",
        })
    new_item.item_type = item_type

    # 提交
    new_item.save()
    
    # 检查是否有循环引用
    if not check_item_circle_quote(item=new_item):
        # 去掉上级物品
        new_item.parent_item = None
        new_item.save()

        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "操作会导致物品循环引用，检查上级物品合理性",
        })

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
    supplier_name = '无'
    if new_item.supplier:
        supplier_name = new_item.supplier.name
    inspection_code_name_list = list(new_item.inspection_codes.values_list('name', flat=True))
    inspection_code_names = '、'.join(inspection_code_name_list)
    add_user_log(
        request=request,
        action=f'新增物品',
        detail=f'''名字：{name}
        物品类型：{item_type.label}
        关联订单号：{order_num}
        关联上级物品：{parent_item_name}
        成本：{fen_to_yuan(cost)}
        销售单价：{fen_to_yuan(sell_price)}
        型号：{model}
        数量：{num}
        检验代码：{inspection_code_names}
        JetPosition：{jet_position}
        ItemNumber：{item_number}
        Description：{description}
        Material：{material}
        Weight：{weight}
        Revision：{revision}
        Uom：{uom}
        LineType：{line_type}
        SupplyType：{supply_type}
        EcoNumber：{eco_number}
        DanieliStandard：{danieli_standard}
        Classification：{classification}
        油漆种类：{paint_type}
        色号：{color_number}
        箱单号：{packing_number}
        合同号：{contract_number}
        供应商：{supplier_name}
        付款：{fen_to_yuan(pay_money_1)}、{fen_to_yuan(pay_money_2)}
        收货：{receive_goods_date_1}、{receive_goods_date_2}
        发货：{send_goods_date_1}、{send_goods_date_2}''',
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
