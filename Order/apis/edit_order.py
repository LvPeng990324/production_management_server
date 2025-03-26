from Order.models import Order
from Order.models import OrderStatus

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.data_covert import str_to_datetime
from utils.data_covert import datetime_to_str
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
    order_start_time = request.json.get('order_start_time')

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": '该订单不存在',
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

    order_start_time = str_to_datetime(order_start_time)
    if order_start_time != order.order_start_time:
        edit_log_str += f'开始时间：{datetime_to_str(order.order_start_time)} -> {datetime_to_str(order_start_time)}\n'
        order.order_start_time = order_start_time

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
