from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Item.models import InspectionCode

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_inspection_code_info_list
from utils.pack_api_data import pack_inspection_code_select_info_list
from utils.permission_check import login_required


@login_required
def get_inspection_code_list(request):
    """ 获取检验代码列表
    GET请求
    """
    current_page = request.GET.get('currentPage') or 1
    page_size = request.GET.get('size') or 10
    name = request.GET.get('name')

    inspection_codes = InspectionCode.objects.all()
    total = inspection_codes.count()

    # 筛选
    if name:
        inspection_codes = inspection_codes.filter(name__contains=name)

    # 加入分页
    paginator = Paginator(inspection_codes, page_size)
    try:
        inspection_codes = paginator.get_page(current_page)
    except PageNotAnInteger:  # 页码非法，返回第一页
        inspection_codes = paginator.get_page(1)
    except EmptyPage:  # 页码超出范围，返回最后一页
        inspection_codes = paginator.get_page(paginator.num_pages)

    inspection_code_info_list = pack_inspection_code_info_list(inspection_codes=inspection_codes)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": total,
        "list": inspection_code_info_list,
    })


@login_required
def get_inspection_code_select_list(request):
    """ 获取检验代码选项列表
    GET 请求
    """
    name = request.GET.get('name')

    inspection_codes = InspectionCode.objects.all()

    # 筛选
    if name:
        inspection_codes = inspection_codes.filter(name__contains=name)

    inspection_code_select_info_list = pack_inspection_code_select_info_list(inspection_codes=inspection_codes)

    return json_response(code=ERROR_CODE.SUCCESS, data=inspection_code_select_info_list)
