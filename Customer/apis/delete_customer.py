from Customer.models import Customer

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
def delete_customer(request):
    """ 删除客户
    POST请求
    """
    customer_id = request.json.get('customer_id')

    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": '该客户不存在',
        })

    # 缓存日志数据
    name = customer.name

    customer.delete()

    # 记录用户日志
    add_user_log(
        request=request,
        action='删除客户',
        detail=f'{name}',
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
