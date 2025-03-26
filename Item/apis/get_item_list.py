from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Item.models import Item

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_item_info_list
from utils.pack_api_data import pack_item_select_info_list
from utils.permission_check import login_required


@login_required
def get_item_list(request):
    """ 获取物品列表
    GET请求
    """
    current_page = request.GET.get('currentPage') or 1
    page_size = request.GET.get('size') or 10
    name = request.GET.get('name')

    items = Item.objects.all()
    total = items.count()

    # 筛选
    if name:
        items = items.filter(name__contains=name)

    # 加入分页
    paginator = Paginator(items, page_size)
    try:
        items = paginator.get_page(current_page)
    except PageNotAnInteger:  # 页码非法，返回第一页
        items = paginator.get_page(1)
    except EmptyPage:  # 页码超出范围，返回最后一页
        items = paginator.get_page(paginator.num_pages)

    item_info_list = pack_item_info_list(items=items)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": total,
        "list": item_info_list,
    })


@login_required
def get_item_select_list(request):
    """ 获取物品选项列表
    GET 请求
    """
    name = request.GET.get('name')

    items = Item.objects.all()

    # 筛选
    if name:
        items = items.filter(name__contains=name)

    item_select_info_list = pack_item_select_info_list(items=items)

    return json_response(code=ERROR_CODE.SUCCESS, data=item_select_info_list)
