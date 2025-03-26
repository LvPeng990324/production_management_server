from Supplier.models import Supplier

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
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

    # 记录用户日志
    add_user_log(
        request=request,
        action='新增供应商',
        detail=f'''名字：{name}
        手机号：{phone}'''
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        'res': 'success',
    })
