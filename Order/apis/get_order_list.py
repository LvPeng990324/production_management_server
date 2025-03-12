from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Order.models import Order

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_order_info_list
from utils.pack_api_data import pack_order_select_info_list


def get_order_list(request):
    """ 获取order列表
    GET请求
    """
    current_page = request.GET.get('currentPage') or 1
    page_size = request.GET.get('size') or 10
    order_num = request.GET.get('order_num')

    orders = Order.objects.all()
    total = orders.count()

    # 筛选
    if order_num:
        orders = orders.filter(order_num__contains=order_num)

    # 加入分页
    paginator = Paginator(orders, page_size)
    try:
        orders = paginator.get_page(current_page)
    except PageNotAnInteger:  # 页码非法，返回第一页
        orders = paginator.get_page(1)
    except EmptyPage:  # 页码超出范围，返回最后一页
        orders = paginator.get_page(paginator.num_pages)

    order_info_list = pack_order_info_list(orders=orders)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": total,
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
