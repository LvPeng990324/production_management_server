from Order.models import Order
from Order.models import OrderStatus

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_order_info_list
from utils.pack_api_data import pack_order_select_info_list


def get_order_list(request):
    """ 获取order列表
    GET请求
    """
    order_num = request.GET.get('order_num')

    orders = Order.objects.all()

    # 筛选
    if order_num:
        orders = orders.filter(order_num__contains=order_num)

    order_info_list = pack_order_info_list(orders=orders)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": len(order_info_list),
        "list": order_info_list,
    })


def get_order_select_list(request):
    """ 获取order选项列表
    GET请求
    """
    order_num = request.GET.get('order_num')

    orders = Order.objects.all()

    # 筛选
    if order_num:
        orders = orders.filter(order_num__contains=order_num)

    order_select_info_list = pack_order_select_info_list(orders=orders)

    return json_response(code=ERROR_CODE.SUCCESS, data=order_select_info_list)
