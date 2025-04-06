from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Customer.models import Customer

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_customer_info_list
from utils.permission_check import login_required


@login_required
def get_customer_list(request):
    """ 获取供应商列表
    GET请求
    """
    current_page = request.GET.get('currentPage') or 1
    page_size = request.GET.get('size') or 10
    name = request.GET.get('name')

    customers = Customer.objects.all()

    # 筛选
    if name:
        customers = customers.filter(name__contains=name)

    total = customers.count()

    # 加入分页
    paginator = Paginator(customers, page_size)
    try:
        customers = paginator.get_page(current_page)
    except PageNotAnInteger:  # 页码非法，返回第一页
        customers = paginator.get_page(1)
    except EmptyPage:  # 页码超出范围，返回最后一页
        customers = paginator.get_page(paginator.num_pages)

    customer_info_list = pack_customer_info_list(customers=customers)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": total,
        "list": customer_info_list,
    })
