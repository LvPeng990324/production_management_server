from Order.models import Order
from Order.models import OrderStatus

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.data_covert import str_to_datetime
from utils.data_covert import str_to_date
from utils.data_covert import datetime_to_str
from utils.data_covert import date_to_str
from utils.data_covert import get_list_default_value
from utils.data_covert import set_list_value_by_index
from utils.data_covert import yuan_to_fen
from utils.data_covert import fen_to_yuan
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
def edit_order(request):
    """ 编辑order
    POST请求
    """
    order_id = request.json.get('order_id')
    order_num = request.json.get('order_num')
    order_status = request.json.get('order_status')
    delivery_date = request.json.get('delivery_date')
    collect_money_1 = yuan_to_fen(request.json.get('collect_money_1'))
    collect_money_2 = yuan_to_fen(request.json.get('collect_money_2'))
    collect_money_3 = yuan_to_fen(request.json.get('collect_money_3'))

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": '该订单不存在',
        })

    # 记录本次修改的内容描述
    edit_log_str = ''

    # 修改
    if order_num != order.order_num:
        edit_log_str += f'订单号：{order.order_num} -> {order_num}\n'
        order.order_num = order_num

    if order_status != order.order_status:
        edit_log_str += f'订单状态：{OrderStatus(order.order_status).label} -> {OrderStatus(order_status).label}\n'
        order.order_status = order_status

    delivery_date = str_to_date(delivery_date)
    if delivery_date != order.delivery_date:
        edit_log_str += f'交货日期：{datetime_to_str(order.delivery_date)} -> {date_to_str(delivery_date)}\n'
        order.delivery_date = delivery_date

    collect_money_list_1 = get_list_default_value(data=order.collect_money_list, index=0, default=0)
    collect_money_list_2 = get_list_default_value(data=order.collect_money_list, index=1, default=0)
    collect_money_list_3 = get_list_default_value(data=order.collect_money_list, index=2, default=0)
    if collect_money_list_1 != collect_money_1:
        edit_log_str += f'收款1：{fen_to_yuan(collect_money_list_1)} -> {fen_to_yuan(collect_money_1)}\n'
        order.collect_money_list = set_list_value_by_index(data=order.collect_money_list, index=0, value=collect_money_1, default=0)
    if collect_money_list_2 != collect_money_2:
        edit_log_str += f'收款2：{fen_to_yuan(collect_money_list_2)} -> {fen_to_yuan(collect_money_2)}\n'
        order.collect_money_list = set_list_value_by_index(data=order.collect_money_list, index=1, value=collect_money_2, default=0)
    if collect_money_list_3 != collect_money_3:
        edit_log_str += f'收款3：{fen_to_yuan(collect_money_list_3)} -> {fen_to_yuan(collect_money_3)}\n'
        order.collect_money_list = set_list_value_by_index(data=order.collect_money_list, index=2, value=collect_money_3, default=0)

    order.save()

    # 记录用户日志
    add_user_log(
        request=request,
        action='编辑订单',
        detail=edit_log_str,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
