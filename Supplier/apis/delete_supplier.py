from Supplier.models import Supplier

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def delete_supplier(request):
    """ 删除供应商
    POST请求
    """
    supplier_id = request.json.get('supplier_id')

    try:
        supplier = Supplier.objects.get(id=supplier_id)
    except Supplier.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": '该订单不存在',
        })

    supplier.delete()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
