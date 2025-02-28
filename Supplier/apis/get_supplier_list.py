from Supplier.models import Supplier

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_supplier_info_list


def get_supplier_list(request):
    """ 获取供应商列表
    GET请求
    """
    name = request.GET.get('name')

    suppliers = Supplier.objects.all()

    # 筛选
    if name:
        suppliers = suppliers.filter(name__contains=name)

    supplier_info_list = pack_supplier_info_list(suppliers=suppliers)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": len(supplier_info_list),
        "list": supplier_info_list,
    })
