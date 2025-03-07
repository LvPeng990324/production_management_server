from Order.models import Order
from Order.models import OrderStatus

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.data_covert import str_to_datetime


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

    # 记录本次修改的内容
    # {字段名: [旧值, 新值]}
    edit_log_record = {}

    # 修改
    if order_num != order.order_num:
        edit_log_record['order_num'] = [order.order_num, order_num]
        order.order_num = order_num

    if order_status != order.order_status:
        edit_log_record['order_status'] = [order.order_status, order_status]
        order.order_status = order_status

    order_start_time = str_to_datetime(order_start_time)
    if order_start_time != order.order_start_time:
        edit_log_record['order_start_time'] = [str(order.order_start_time), str(order_start_time)]
        order.order_start_time = order_start_time

    order.save()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
