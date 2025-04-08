from Order.models import Order
from Order.models import OrderStatus

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required
from utils.data_covert import yuan_to_fen
from utils.data_covert import date_to_str
from utils.data_covert import str_to_date


@login_required
def add_order(request):
    """ 新增order
    POST请求
    """
    order_num = request.json.get('order_num')
    order_status = request.json.get('order_status')
    delivery_date = str_to_date(request.json.get('delivery_date'))
    collect_money_1 = yuan_to_fen(request.json.get('collect_money_1'))
    collect_money_2 = yuan_to_fen(request.json.get('collect_money_2'))
    collect_money_3 = yuan_to_fen(request.json.get('collect_money_3'))

    Order.objects.create(
        order_num=order_num,
        order_status=order_status,
        delivery_date=delivery_date,
        collect_money_list=[collect_money_1, collect_money_2, collect_money_3],
        worker_id=request.session.get('user_id'),
    )

    # 记录用户日志
    add_user_log(
        request=request,
        action='新增订单',
        detail=f'''订单号：{order_num}
        订单状态：{OrderStatus(order_status).label}
        交货日期：{date_to_str(delivery_date)}
        收款：{collect_money_1}、{collect_money_2}、{collect_money_3}'''
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
