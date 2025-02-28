from Item.models import TechnicalChange

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_technical_change_info_list


def get_technical_change_list(request):
    """ 获取技术变更列表
    GET请求
    """
    name = request.GET.get('name')

    technical_changes = TechnicalChange.objects.all()

    # 筛选
    if name:
        technical_changes = technical_changes.filter(name__contains=name)

    technical_change_info_list = pack_technical_change_info_list(technical_changes=technical_changes)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": len(technical_change_info_list),
        "list": technical_change_info_list,
    })
