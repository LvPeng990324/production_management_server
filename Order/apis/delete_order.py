from Order.models import Order
from Order.models import OrderStatus

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
def delete_order(request):
    """ 删除order
    POST请求
    """
    order_id = request.json.get('order_id')

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "msg": '该订单不存在',
        })

    # 缓存日志数据
    order_num = order.order_num

    order.delete()

    # 记录用户日志
    add_user_log(
        request=request,
        action='删除订单',
        detail=f'{order_num}',
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
