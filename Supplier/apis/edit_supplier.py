from Supplier.models import Supplier

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def edit_supplier(request):
    """ 编辑供应商
    POST请求
    """
    supplier_id = request.json.get('supplier_id')
    name = request.json.get('name')
    phone = request.json.get('phone')

    try:
        supplier = Supplier.objects.get(id=supplier_id)
    except Supplier.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
        "msg": '该供应商不存在',
    })

    # 记录本次修改的内容
    # {字段名: [旧值, 新值]}
    edit_log_record = {}

    # 修改
    if name != supplier.name:
        edit_log_record['name'] = [supplier.name, name]
        supplier.name = name

    if phone != supplier.phone:
        edit_log_record['phone'] = [supplier.phone, phone]
        supplier.phone = phone

    supplier.save()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
