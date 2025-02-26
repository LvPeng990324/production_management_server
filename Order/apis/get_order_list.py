from Order.models import Order
from Order.models import OrderStatus

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_order_info_list


def get_order_list(request):
    """ 获取order列表
    GET请求
    """

    orders = Order.objects.all()

    order_info_list = pack_order_info_list(orders=orders)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": len(order_info_list),
        "list": order_info_list,
    })
