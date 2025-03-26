from Supplier.models import Supplier

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
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

    # 记录本次修改的内容描述
    edit_log_str = ''

    # 修改
    if name != supplier.name:
        edit_log_str += f'名字：{supplier.name} -> {name}\n'
        supplier.name = name

    if phone != supplier.phone:
        edit_log_str += f'手机号：{supplier.phone} -> {phone}\n'
        supplier.phone = phone

    supplier.save()

    # 记录用户日志
    add_user_log(
        request=request,
        action='编辑供应商',
        detail=edit_log_str,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
