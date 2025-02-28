from Supplier.models import Supplier

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def add_supplier(request):
    """ 新增供应商
    POST请求
    """
    name = request.json.get('name')
    phone = request.json.get('phone')

    Supplier.objects.create(
        name=name,
        phone=phone,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        'res': 'success',
    })
