from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from StoreHouse.models import StoreHouse

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_store_house_info_list
from utils.permission_check import login_required


@login_required
def get_store_house_list(request):
    """ 获取库存列表
    GET请求
    """
    current_page = request.GET.get('currentPage') or 1
    page_size = request.GET.get('size') or 10
    name = request.GET.get('name')

    store_houses = StoreHouse.objects.all()

    # 筛选
    if name:
        store_houses = store_houses.filter(item__name__contains=name)

    total = store_houses.count()

    # 加入分页
    paginator = Paginator(store_houses, page_size)
    try:
        store_houses = paginator.get_page(current_page)
    except PageNotAnInteger:  # 页码非法，返回第一页
        store_houses = paginator.get_page(1)
    except EmptyPage:  # 页码超出范围，返回最后一页
        store_houses = paginator.get_page(paginator.num_pages)

    store_house_info_list = pack_store_house_info_list(store_houses=store_houses)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": total,
        "list": store_house_info_list,
    })
