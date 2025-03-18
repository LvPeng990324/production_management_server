from Order.models import Order
from Order.models import OrderStatus

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log


def add_order(request):
    """ 新增order
    POST请求
    """
    order_num = request.json.get('order_num')
    order_status = request.json.get('order_status')
    order_start_time = request.json.get('order_start_time')

    Order.objects.create(
        order_num = order_num,
        order_status = order_status,
        order_start_time = order_start_time,
    )

    # 记录用户日志
    add_user_log(
        request=request,
        action='新增订单',
        detail=f'''订单号：{order_num}
        订单状态：{OrderStatus(order_status).label}
        开始时间：{order_start_time}'''
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
