from Order.models import Order
from Order.models import OrderStatus

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.data_covert import str_to_datetime


def delete_order(request):
    """ 删除order
    POST请求
    """
    order_id = request.json.get('order_id')

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": '该订单不存在',
        })

    order.delete()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
