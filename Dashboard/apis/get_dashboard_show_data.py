from Order.models import Order
from Supplier.models import Supplier

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.permission_check import login_required


@login_required
def get_dashboard_show_data(request):
    """ 获取首页展示数据
    GET请求
    """
    # 统计订单数量
    order_count = Order.objects.all().count()

    # 统计供应商数量
    supplier_count = Supplier.objects.all().count()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "order_count": order_count,
        "supplier_count": supplier_count,
    })
