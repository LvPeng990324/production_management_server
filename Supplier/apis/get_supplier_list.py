from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Supplier.models import Supplier

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_supplier_info_list
from utils.pack_api_data import pack_supplier_select_info_list
from utils.permission_check import login_required


@login_required
def get_supplier_list(request):
    """ 获取供应商列表
    GET请求
    """
    current_page = request.GET.get('currentPage') or 1
    page_size = request.GET.get('size') or 10
    name = request.GET.get('name')

    suppliers = Supplier.objects.all()

    # 筛选
    if name:
        suppliers = suppliers.filter(name__contains=name)

    total = suppliers.count()

    # 加入分页
    paginator = Paginator(suppliers, page_size)
    try:
        suppliers = paginator.get_page(current_page)
    except PageNotAnInteger:  # 页码非法，返回第一页
        suppliers = paginator.get_page(1)
    except EmptyPage:  # 页码超出范围，返回最后一页
        suppliers = paginator.get_page(paginator.num_pages)

    supplier_info_list = pack_supplier_info_list(suppliers=suppliers)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": total,
        "list": supplier_info_list,
    })


@login_required
def get_supplier_select_list(request):
    """ 获取供应商选项列表
    GET请求
    """
    supplier_name = request.GET.get('supplier_name')

    suppliers = Supplier.objects.all()

    # 筛选
    if supplier_name:
        suppliers = suppliers.filter(name__contains=supplier_name)

    supplier_select_info_list = pack_supplier_select_info_list(suppliers=suppliers)

    return json_response(code=ERROR_CODE.SUCCESS, data=supplier_select_info_list)
