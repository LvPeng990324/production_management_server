from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Purchase.models import PurchaseRequirement

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_purchase_requirement_info_list
from utils.permission_check import login_required


@login_required
def get_purchase_requirement_list(request):
    """ 获取采购需求列表
    GET请求
    """
    current_page = request.GET.get('currentPage') or 1
    page_size = request.GET.get('size') or 10
    iten_name = request.GET.get('iten_name')

    purchase_requirements = PurchaseRequirement.objects.all()

    # 筛选
    if iten_name:
        purchase_requirements = purchase_requirements.filter(item__name__contains=iten_name)

    total = purchase_requirements.count()

    # 加入分页
    paginator = Paginator(purchase_requirements, page_size)
    try:
        purchase_requirements = paginator.get_page(current_page)
    except PageNotAnInteger:  # 页码非法，返回第一页
        purchase_requirements = paginator.get_page(1)
    except EmptyPage:  # 页码超出范围，返回最后一页
        purchase_requirements = paginator.get_page(paginator.num_pages)

    purchase_requirement_info_list = pack_purchase_requirement_info_list(purchase_requirements=purchase_requirements)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": total,
        "list": purchase_requirement_info_list,
    })
