from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Item.models import TechnicalChange

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_technical_change_info_list
from utils.permission_check import login_required


@login_required
def get_technical_change_list(request):
    """ 获取技术变更列表
    GET请求
    """
    current_page = request.GET.get('currentPage') or 1
    page_size = request.GET.get('size') or 10
    name = request.GET.get('name')

    technical_changes = TechnicalChange.objects.all()
    total = technical_changes.count()

    # 筛选
    if name:
        technical_changes = technical_changes.filter(name__contains=name)

    # 加入分页
    paginator = Paginator(technical_changes, page_size)
    try:
        technical_changes = paginator.get_page(current_page)
    except PageNotAnInteger:  # 页码非法，返回第一页
        technical_changes = paginator.get_page(1)
    except EmptyPage:  # 页码超出范围，返回最后一页
        technical_changes = paginator.get_page(paginator.num_pages)

    technical_change_info_list = pack_technical_change_info_list(technical_changes=technical_changes)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": total,
        "list": technical_change_info_list,
    })
