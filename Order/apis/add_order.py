from Order.models import Order
from Order.models import OrderStatus

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


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

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
