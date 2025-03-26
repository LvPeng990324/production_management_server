from Supplier.models import Supplier

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
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

    # 缓存日志数据
    name = supplier.name

    supplier.delete()

    # 记录用户日志
    add_user_log(
        request=request,
        action='删除供应商',
        detail=f'{name}',
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
