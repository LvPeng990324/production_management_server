from Item.models import InspectionCode

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_inspection_code_info_list


def get_inspection_code_list(request):
    """ 获取检验代码列表
    GET请求
    """
    name = request.GET.get('name')

    inspection_codes = InspectionCode.objects.all()

    # 筛选
    if name:
        inspection_codes = inspection_codes.filter(name__contains=name)

    inspection_code_info_list = pack_inspection_code_info_list(inspection_codes=inspection_codes)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": len(inspection_code_info_list),
        "list": inspection_code_info_list,
    })
